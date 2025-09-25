# datafun-05-sql
Data Analytics Fundamentals - Week 5 of 7 - Project

# Project Initialization

## Cloned my Repo from GitHub to my Machine
1. Copied URL from GitHub
2. Used following code for implementing to my own machine
```shell
cd C:\Repos
git clone URL
```

## Added `.gitignore` and `requirements.txt` Files
1. Added these files directly in VS Code
2. Added contents from Dr. Case's example Repo
3. Add - Commit - Push

## Creating the Virtual Environment (Activate EACH TIME you enter the Repo)
1. Used the following script to create then activate the `.venv`:
```shell
py -m venv .venv
.\.venv\Scripts\activate
```
2. Add - Commit - Push

## Installed Dependency Packages and Upgrades (Upgrade EACH TIME you enter the Repo)
1. Upgraded the Setuptools Wheel
```shell
pip install --upgrade setuptools wheel
```
2. Upgraded the `requirements.txt` imports
```shell
pip install --upgrade -r requirements.txt
```
3. Add - Commit - Push

# Project Work
## Implementing a Logger
1. Added `utils_logger.py` to my repo, filling it with contents in the example repo.
   1. I did this because I believe it will be nice to have later in the project.
2. Add - Commit - Push

## Planning the Data Sources
1. Created a folder to house the data.
   1. This is the `data` folder.
2. Created a CSV for the authors and books.
   1. These are called `authors.csv` and `books.csv` respectively and are filled with example data, as this is a guided project.
3. Add - Commit - Push

## Planning the Creation Files
1. Created the `sql_create` folder to house my SQL scripts
2. Created the following tables named for their purposes
   1. `01_drop_tables.sql`: drops tables within my database if they already exist
   2. `02_create_tables.sql`: creates new tables based on data within the repo.
   3. `03_insert_records.sql`: inserts new records to the table.
3. These have been populated with content from the example repo.
4. Add - Commit - Push

## Writing the Setup Script
1. Created the setup script using pieces from the module workthrough.
   1. This script creates a database, then creates tables, then inserts records into those tables.
2. Add - Commit - Push