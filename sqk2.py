print("before db connection")
import mysql.connector

mydb=mysql.connector.connect(host="localhost", user='siva', passwd='Padhar!234', database='world')
print("after db connection")

# Create a cursor
cursor = mydb.cursor()

# Define your SQL query
query = "SELECT * FROM world.city"

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
mydb.close()
