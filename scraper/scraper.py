import time
from io import StringIO

import pandas as pd
from cloudscraper import create_scraper
from pandas import DataFrame
from sqlalchemy import false

LEAGUE_URLS = {
    "Premier League": {"url": "https://fbref.com/en/comps/9/Premier-League-Stats",
                       "attribute_id": "results2025-202691_overall"},
    "La Liga": {"url": "https://fbref.com/en/comps/12/La-Liga-Stats",
                "attribute_id": "results2025-2026121_overall"},
    "Bundesliga": {"url": "https://fbref.com/en/comps/20/Bundesliga-Stats",
                   "attribute_id": "results2025-2026201_overall"},
    "Serie A": {"url": "https://fbref.com/en/comps/11/Serie-A-Stats",
                "attribute_id": "results2025-2026111_overall"},
    "Ligue 1": {"url": "https://fbref.com/en/comps/13/Ligue-1-Stats",
                "attribute_id": "results2025-2026131_overall"}
}

def scrape_league_data() -> None:
    df_list = []
    scraper = create_scraper()
    for league, data in LEAGUE_URLS.items():
        response = scraper.get(data["url"]).text

        df = pd.read_html(StringIO(response), attrs={"id": data["attribute_id"]}, flavor="lxml")[0]
        df.insert(0, "competition_name", league)
        if "Last 5" not in df.columns:
            df.insert(15, "Last 5", pd.NA)

        df_list.append(df)

        # delay next request to avoid falling into request rate problem
        time.sleep(5)

    combined_df = pd.concat(df_list)
    # Drop columns that will be calculated by the DB (except Pts/MP, Goalkeeper and Notes)
    combined_df.drop(["GD", "xGD", "Pts/MP", "Goalkeeper", "Notes"], axis=1, inplace=True)
    combined_df = rename_df_cols(combined_df)
    combined_df.fillna(0, inplace=True)

    combined_df.to_csv("../data/data.csv", index=False, mode="w")

def rename_df_cols(df: DataFrame) -> DataFrame:
    # rename dataframe cols to match DB cols
    df = df.rename(columns={
        "Rk": "position",
        "Squad": "team_name",
        "MP": "matches_played",
        "W": "wins",
        "D": "draws",
        "L": "losses",
        "GF": "goals_scored",
        "GA": "goals_conceded",
        "Pts": "points",
        "xG": "expected_goals",
        "xGA": "expected_goals_conceded",
        "xGD/90": "expected_goals_diff_90_min",
        "Last 5": "last_5",
        "Attendance": "attendance",
        "Top Team Scorer": "top_team_scorer"
    })

    return df


def main() -> None:
    scrape_league_data()

if __name__ == '__main__':
    main()
