import time
from http.client import responses
from typing import List

import requests
import json

BASE_URL = 'https://fbrapi.com'
# Codes used to describe leagues we are looking for
COUNTRY_CODES = ["ITA", "ESP", "FRA", "GER", "ENG"]

def get_league_info(api_key: str) -> dict[str, dict]:
    url = BASE_URL + "/leagues"
    headers = {'X-API-Key': api_key}

    league_info = {}

    for country in COUNTRY_CODES:
        response = requests.get(url, params={"country_code": country}, headers=headers)
        if response.status_code == 200:
            league_info[country] = {}

            # get data to describe tier 1 leagues in given countries
            league_data = response.json()["data"][0]['leagues'][0]

            league_info[country] = {
                "league_id": league_data["league_id"],
                "competition_name": league_data["competition_name"]
            }

            # add a delay as stated in FBR API docs to prevent restrictions
            time.sleep(3)

    return league_info

def main() -> None:
    # generate unique API Key needed to scrape the data
    response = requests.post(BASE_URL + '/generate_api_key')
    FBR_API_KEY = response.json().get('api_key')

    league_ids = get_league_info(FBR_API_KEY)

    print(json.dumps(league_ids, indent=4))

    # print(response.status_code)
    #
    # print(json.dumps(response.json(), indent=4))


if __name__ == '__main__':
    main()
