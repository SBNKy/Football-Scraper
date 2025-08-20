import os
import time
from io import StringIO

import pandas as pd
from cloudscraper import create_scraper
from pandas import DataFrame

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

def scrape_league_data() -> DataFrame:
    df_list = []
    scraper = create_scraper()

    for league, data in LEAGUE_URLS.items():
        response = scraper.get(data["url"]).text
        print(response)
        df = pd.read_html(StringIO(response), attrs={"id": data["attribute_id"]}, flavor="lxml")[0]
        df.insert(0, "Competition name", league)
        if "Last 5" not in df.columns:
            df.insert(15, "Last 5", pd.NA)

        df_list.append(df)

        time.sleep(5)

    combined_df = pd.concat(df_list)
    combined_df.to_csv("../data/data.csv")

    return combined_df


def main() -> None:
    scrape_league_data()

if __name__ == '__main__':
    main()
