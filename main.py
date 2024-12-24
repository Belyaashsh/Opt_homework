import mysql.connector
from mysql.connector import Error
import pymysql

def create_connection(host_name, user_name, user_password, db_name):
    try:
        connection = pymysql.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error: '{e}' occurred")
        return None


def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: '{e}' occurred")

def read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error: '{e}' occurred")
        return None

# Connection details
connection = create_connection("localhost", "belyaashsh", "12345678", "HW_DB")

if connection:
    # Example: Fetch all students
    select_students = "SELECT * FROM Students;"
    students = read_query(connection, select_students)
    print("Students:")
    for student in students:
        print(student)

    # Example: Add a new grade
    add_grade_query = """
    INSERT INTO Grades (Student_id, Subject_id, Grade) 
    VALUES (%s, %s, %s);
    """
    new_grade = (1, 2, 'A')
    execute_query(connection, add_grade_query, new_grade)

    # Example: Join query to fetch student grades
    join_query = """
    SELECT Students.name, Subjects.subject_name, Grades.Grade 
    FROM Grades
    INNER JOIN Students ON Grades.Student_id = Students.id
    INNER JOIN Subjects ON Grades.Subject_id = Subjects.id;
    """
    grades = read_query(connection, join_query)
    print("\nStudent Grades:")
    for grade in grades:
        print(grade)

    # Close connection
    connection.close()
