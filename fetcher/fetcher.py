import time
from http.client import responses
from typing import List

import requests
import json

BASE_URL = 'https://fbrapi.com'
# Codes used to describe leagues we are looking for
COUNTRY_CODES = ["ITA", "ESP", "FRA", "GER", "ENG"]

def get_league_ids(api_key: str) -> dict[str, int]:
    url = BASE_URL + "/leagues"
    headers = {'X-API-Key': api_key}

    league_ids = {}

    for country in COUNTRY_CODES:
        response = requests.get(url, params={"country_code": country}, headers=headers)
        if response.status_code == 200:
            # get data to describe tier 1 leagues in given countries
            league_data = response.json()["data"][0]['leagues'][0]
            competition_name = league_data["competition_name"]
            league_id = league_data["league_id"]

            league_ids[competition_name] = league_id

            # add a delay as stated in FBR API docs to prevent restrictions
            time.sleep(3)

    return league_ids

def main() -> None:
    # generate unique API Key needed to scrape the data
    response = requests.post(BASE_URL + '/generate_api_key')
    FBR_API_KEY = response.json().get('api_key')

    league_ids = get_league_ids(FBR_API_KEY)

    print(league_ids)

    # print(response.status_code)
    #
    # print(json.dumps(response.json(), indent=4))


if __name__ == '__main__':
    main()
