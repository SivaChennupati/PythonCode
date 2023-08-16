import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'siva',
    'port': '3306',
    'passwd': 'Padhar!234',
    'database': 'world'
}

# Connect to the database
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Connected to the database")

        # Create a cursor
        cursor = connection.cursor()

        # Define the SQL query
        query = "SELECT * FROM CITY"

        # Execute the query
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the retrieved data
        for row in rows:
            print(row)

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")

