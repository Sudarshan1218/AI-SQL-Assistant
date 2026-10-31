
# AI-Powered SQL Assistant

An interactive application that converts natural-language questions into SQL queries and executes them on a SQLite database.

## Project Overview

The AI-Powered SQL Assistant allows users to interact with a student database using simple English questions instead of manually writing SQL queries.

The application recognises supported question patterns, generates SQL queries, validates them, and displays the results through an interactive Streamlit interface.

## Features

- Natural Language to SQL conversion
- SQLite database integration
- Interactive Streamlit interface
- Suggested sample questions
- Display generated SQL queries
- Tabular query results
- Read-only SQL execution
- Basic SQL injection and multiple-statement safeguards

## Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- Regular Expressions

## Project Structure

AI-SQL-Assistant/
|
|-- app.py
|-- ai_engine.py
|-- database.py
|-- sql_executor.py
|-- requirements.txt
|-- README.md
|
|-- data/
    |-- students.db

## Example Questions

1. Show all students
2. Show students from Nashik
3. Show students with marks above 80
4. Show students with marks below 75
5. Show highest marks
6. Show average marks
7. Count students

## How to Run the Project

### 1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

### 2. Open the project folder

cd AI-SQL-Assistant

### 3. Create a virtual environment

python -m venv venv

### 4. Activate the virtual environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1

### 5. Install dependencies

pip install -r requirements.txt

### 6. Run the application

streamlit run app.py

## Future Improvements

- Support more natural-language question patterns
- Add more database tables
- Improve query understanding
- Add data visualisation
- Support user-uploaded databases

## Author

Developed as a Python, SQL and Natural Language Processing portfolio project.
