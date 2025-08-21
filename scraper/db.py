import os
from dotenv import load_dotenv
import psycopg
import pandas as pd

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")


def test_connection() -> bool:
    with psycopg.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD, port=DB_PORT) as conn:
        print(f"Database {DB_NAME} exists.")
        with conn.cursor() as curr:
            curr.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                    AND table_name = 'players'
                )
            """)

            if curr.fetchone()[0]:
                print('"Players" Table exists.')

            curr.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                    AND table_name = 'teams')
             """)

            if curr.fetchone()[0]:
                print('"Teams" Table exists.')

            return True

def read_csv(path="../data/data.csv"):
    df = pd.read_csv(path)
    tuples = [tuple(row) for row in df.to_numpy()]
    print(tuples[0])
    cols = ','.join(list(df.columns))
    print(cols)
    with psycopg.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD, port=DB_PORT) as conn:
        with conn.cursor() as curr:
            pass
            curr.execute("INSERT INTO ")


def main() -> None:
    test_connection()
    read_csv()


if __name__ == '__main__':
    main()
