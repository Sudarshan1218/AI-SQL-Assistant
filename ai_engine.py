
import re


def generate_sql(question):
    question = question.lower().strip()

    # Students from a particular city
    city_match = re.search(r"\b(?:from|in)\s+(nashik|pune|mumbai)\b", question)
    if city_match:
        city = city_match.group(1).title()
        return f"SELECT * FROM students WHERE city = '{city}'"

    # Students with marks above a number
    marks_match = re.search(r"(?:above|greater than|more than)\s+(\d+)", question)
    if marks_match and "mark" in question:
        marks = int(marks_match.group(1))
        return f"SELECT * FROM students WHERE marks > {marks}"

    # Students with marks below a number
    marks_match = re.search(r"(?:below|less than)\s+(\d+)", question)
    if marks_match and "mark" in question:
        marks = int(marks_match.group(1))
        return f"SELECT * FROM students WHERE marks < {marks}"

    # Highest marks
    if "highest marks" in question or "top marks" in question:
        return "SELECT * FROM students ORDER BY marks DESC LIMIT 1"

    # Average marks
    if "average marks" in question or "average score" in question:
        return "SELECT AVG(marks) AS average_marks FROM students"

    # Count students
    if "count" in question or "how many students" in question:
        return "SELECT COUNT(*) AS total_students FROM students"

    # Show all students (check this last)
    if any(word in question for word in ["all students", "show students", "list students"]):
        return "SELECT * FROM students"

    return None
