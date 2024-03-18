import psycopg2
import sys

def getAllStudents():
#Retrieves and displays all records from the students table.
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
    # Execute SQL query
    cursor.execute("select * from students ORDER BY student_id ASC")

    # Fetch and process results
    query = cursor.fetchall()

    #Printing results

    print("Displaying all records from the students table")
    for item in query:
        print(item)

    cursor.close()
    connection.close()
