import pandas as pd


def main():
    team_url = "https://fbref.com/en/squads/5bfb9659/Leeds-United-Stats"

    # Sendeing HTTP GET-request to webpage
    response = requests.get(team_url)

    # check for success response (statuscode 200)
    if response.status_code == 200:
        print("Successfully retrieved page")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
