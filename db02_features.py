# demonstrates the ability to run SQL Scripts to interact with fields, update records, 
# delete records, and maybe add additional columns

# This script deletes records from the "books" table if they were published before 1900
# This script also updates JRR Tolkien's record so his author ID matches in each record.

import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("authors_books.sqlite3")

def delete_and_update_records():
    """Function to read and execute SQL statements to create tables"""
    SQL_CHANGES = ["delete_records.sql", "update_records.sql"]
    try:
        with sqlite3.connect(db_file) as conn:
            for name in SQL_CHANGES:
                sql_file = pathlib.Path("sql_features", name)  # adjust folder name if different
                if not sql_file.exists():
                    print(f"Missing SQL file: {sql_file}")
                    continue
                with open(sql_file, "r", encoding="utf-8") as file:
                    sql_script = file.read()
                conn.executescript(sql_script)
                print(f"Executed {name} successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)


def main():
    delete_and_update_records()

if __name__ == "__main__":
    main()   