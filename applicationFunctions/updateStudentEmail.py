import psycopg2
import sys

def updateStudentEmail(student_id, email):
#Updates the email address for a student with the specified student_id.
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
    # Execute SQL update
    command = "UPDATE students SET email = %s WHERE student_id = %s"
    cursor.execute(command, (email, student_id))
    connection.commit()

    cursor.close()
    connection.close()