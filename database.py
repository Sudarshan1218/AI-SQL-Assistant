
import sqlite3
import os

# Create data folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Create data folder if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

# Database file location
DB_PATH = os.path.join(DATA_DIR, "students.db")


def create_database():

    # Connect to SQLite database
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    # Create students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            branch TEXT NOT NULL,
            marks INTEGER,
            age INTEGER,
            city TEXT
        )
    """)

    # Insert sample student records
    cursor.executemany("""
        INSERT OR IGNORE INTO students
        (student_id, name, branch, marks, age, city)
        VALUES (?, ?, ?, ?, ?, ?)
    """, [
        (1, "Rahul", "Computer", 85, 20, "Nashik"),
        (2, "Priya", "IT", 92, 21, "Pune"),
        (3, "Amit", "Computer", 76, 20, "Mumbai"),
        (4, "Sneha", "Mechanical", 89, 22, "Nashik"),
        (5, "Rohan", "IT", 68, 21, "Pune"),
        (6, "Neha", "Computer", 95, 20, "Nashik"),
        (7, "Karan", "Civil", 72, 22, "Mumbai"),
        (8, "Pooja", "IT", 88, 21, "Nashik")
    ])

    # Save changes
    connection.commit()

    # Close connection
    connection.close()

    print("Database created successfully!")


if __name__ == "__main__":
    create_database()
