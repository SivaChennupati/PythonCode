rt = '3306'
password = 'Padhar!234'
database = 'world'

# Connect to the database
connection = _mysql_connector.connect(host='localhost',user='siva',password='Padhar!234', database="world")

# Create a cursor
cursor = connection.cursor()

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
connection.close()

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
