import pandas as pd
import requests


def main():
    df = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats",
        attrs={"id": "results2025-202691_overall"})[0]
    print(df.head())

if __name__ == "__main__":
    main()
