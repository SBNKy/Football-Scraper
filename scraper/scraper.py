import pandas as pd
from bs4 import BeautifulSoup
from cloudscraper import create_scraper
from six import StringIO

LEAGUE_URLS = {
    "Premier League": "https://fbref.com/en/comps/9/Premier-League-Stats",
    "La Liga": "https://fbref.com/en/comps/12/La-Liga-Stats",
    "Bundesliga": "https://fbref.com/en/comps/20/Bundesliga-Stats",
    "Serie A": "https://fbref.com/en/comps/11/Serie-A-Stats",
    "Ligue 1": "https://fbref.com/en/comps/13/Ligue-1-Stats"
}

def scrape_league_data() -> None:
    scraper = create_scraper()
    response = scraper.get("https://fbref.com/en/comps/9/Premier-League-Stats").text
    df = pd.read_html(StringIO(response), attrs={"id": "results2025-202691_overall"})[0]

    # soup = BeautifulSoup(response, features="lxml")
    # table = soup.find_all("table")
    print(df.head())




def main() -> None:
    scrape_league_data()



if __name__ == '__main__':
    main()
