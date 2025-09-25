import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("authors_books.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    # This will drop any tables in the database, then create new ones.
    SQL_CREATION = ["01_drop_tables.sql", "02_create_tables.sql", "03_insert_records.sql"]
    try:
        with sqlite3.connect(db_file) as conn:
            for name in SQL_CREATION:
                sql_file = pathlib.Path("sql_create", name)  # adjust folder name if different
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
    create_database()
    create_tables()

if __name__ == "__main__":
    main()