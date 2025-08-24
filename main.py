import os

from scraper.scraper import scrape_league_data
from scraper.db import test_connection, read_csv

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "data", "data.csv")

def main():
    scrape_league_data(DATA_PATH)
    if test_connection():
        read_csv(DATA_PATH)

if __name__ == "__main__":
    main()
