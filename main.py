import re
import pymysql
from pymysql.err import IntegrityError

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

def validate_data(data, regex):
    if not re.fullmatch(regex, data):
        raise ValueError(f"Invalid input: {data}")

def create_student(connection, name, group_name):
    validate_data(name, r"^[А-Яа-я\s]+$")
    validate_data(group_name, r"^[А-Яа-яA-Za-z0-9\-]+$")

    query = "INSERT INTO Students (name, group_name) VALUES (%s, %s)"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (name, group_name))
            connection.commit()
            print("Student created successfully")
    except IntegrityError as e:
        print(f"Error: {e}")

def read_students(connection):
    query = "SELECT * FROM Students"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

def update_student(connection, student_id, name=None, group_name=None):
    if name:
        validate_data(name, r"^[А-Яа-я\s]+$")
    if group_name:
        validate_data(group_name, r"^[А-Яа-яA-Za-z0-9\-]+$")

    updates = []
    values = []

    if name:
        updates.append("name = %s")
        values.append(name)
    if group_name:
        updates.append("group_name = %s")
        values.append(group_name)
    values.append(student_id)

    query = f"UPDATE Students SET {', '.join(updates)} WHERE id = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, tuple(values))
            connection.commit()
            print("Student updated successfully")
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

def delete_student(connection, student_id):
    query = "DELETE FROM Students WHERE id = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (student_id,))
            connection.commit()
            print("Student deleted successfully")
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

def create_subject(connection, subject_name, grading_system, hours_for_semesters):
    validate_data(subject_name, r"^[А-Яа-яA-Za-z\s]+$")
    validate_data(grading_system, r"^[А-Яа-яA-Za-z\s]+$")
    if not isinstance(hours_for_semesters, int):
        raise ValueError("Hours for semesters must be an integer")

    query = "INSERT INTO Subjects (subject_name, grading_system, hours_for_semesters) VALUES (%s, %s, %s)"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (subject_name, grading_system, hours_for_semesters))
            connection.commit()
            print("Subject created successfully")
    except IntegrityError as e:
        print(f"Error: {e}")

def read_subjects(connection):
    query = "SELECT * FROM Subjects"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

def update_subject(connection, subject_id, subject_name=None, grading_system=None, hours_for_semesters=None):
    if subject_name:
        validate_data(subject_name, r"^[А-Яа-яA-Za-z\s]+$")
    if grading_system:
        validate_data(grading_system, r"^[А-Яа-яA-Za-z\s]+$")
    if hours_for_semesters is not None and not isinstance(hours_for_semesters, int):
        raise ValueError("Hours for semesters must be an integer")

    updates = []
    values = []

    if subject_name:
        updates.append("subject_name = %s")
        values.append(subject_name)
    if grading_system:
        updates.append("grading_system = %s")
        values.append(grading_system)
    if hours_for_semesters is not None:
        updates.append("hours_for_semesters = %s")
        values.append(hours_for_semesters)
    values.append(subject_id)

    query = f"UPDATE Subjects SET {', '.join(updates)} WHERE id = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, tuple(values))
            connection.commit()
            print("Subject updated successfully")
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

def delete_subject(connection, subject_id):
    query = "DELETE FROM Subjects WHERE id = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (subject_id,))
            connection.commit()
            print("Subject deleted successfully")
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

def create_grade(connection, student_id, subject_id, grade):
    validate_data(grade, r"^[A-Za-z0-9]+$")

    query = "INSERT INTO Grades (Student_id, Subject_id, Grade) VALUES (%s, %s, %s)"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (student_id, subject_id, grade))
            connection.commit()
            print("Grade created successfully")
    except IntegrityError as e:
        print(f"Error: {e}")

def read_grades(connection):
    query = "SELECT * FROM Grades"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

def update_grade(connection, student_id, subject_id, grade):
    validate_data(grade, r"^[A-Za-z0-9]+$")

    query = "UPDATE Grades SET Grade = %s WHERE Student_id = %s AND Subject_id = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (grade, student_id, subject_id))
            connection.commit()
            print("Grade updated successfully")
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

def delete_grade(connection, student_id, subject_id):
    query = "DELETE FROM Grades WHERE Student_id = %s AND Subject_id = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (student_id, subject_id))
            connection.commit()
            print("Grade deleted successfully")
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

connection = create_connection("localhost", "your_user", "your_password", "HW_DB")

if connection:
    try:
        # Select Students
        students = read_students(connection)
        print("\nStudents:")
        for student in students:
            print(student)

        # Select Subjects
        subjects = read_subjects(connection)
        print("\nSubjects:")
        for subject in subjects:
            print(subject)

        # Select Grades
        grades = read_grades(connection)
        print("\nGrades:")
        for grade in grades:
            print(grade)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close connection
        connection.close()
