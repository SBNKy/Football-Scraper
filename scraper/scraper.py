import json

import requests
from bs4 import BeautifulSoup

URLS = {
    "Premier League": "https://fbref.com/en/comps/9/Premier-League-Stats",
    "La Liga": "https://fbref.com/en/comps/12/La-Liga-Stats",
    "Bundesliga": "https://fbref.com/en/comps/20/Bundesliga-Stats",
    "Serie A": "https://fbref.com/en/comps/11/Serie-A-Stats",
    "Ligue 1": "https://fbref.com/en/comps/13/Ligue-1-Stats"
}

def scrape_league_data() -> None:
    pass


def main() -> None:
    for league, url in URLS.items():
        print(league, url)
    response = requests.get(URLS.get("Premier League"), 'html.parser')
    print(response.status_code)
    print(response.text)
    # print(json.dumps(response.json(), indent=4))

if __name__ == '__main__':
    main()
