import psycopg2
import sys

def addStudent(first_name, last_name, email, enrollment_date):
#Inserts a new student record into the students table.
    #Establishing connection
    try:
        connection = psycopg2.connect(
                                host = "localhost", 
                                user = "postgres", 
                                password = "postgres",
                                database = "3005A3")
        
    except psycopg2.Error as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(e)
        sys.exit(1)
        
    cursor = connection.cursor()
    # Execute SQL insertion
    command = "INSERT INTO students (first_name,last_name,email,enrollment_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(command, (first_name, last_name, email, enrollment_date))
    connection.commit()

    cursor.close()
    connection.close()
