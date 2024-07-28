import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )

        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()

            # SQL statement to create the database
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            # Execute the SQL statement
            cursor.execute(create_db_query)

            # Print success message
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Print error message if there is an exception
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor and cursor.is_connected():
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

# Run the function to create the database
create_database()
