import mysql.connector

# Establish a connection to MySQL
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='new_password'
)

# Create a cursor object to execute SQL queries
cursorObject = dataBase.cursor()

# Create a new database named 'mysql' (fixing the typo)
cursorObject.execute('CREATE DATABASE eldero ')

# Close the cursor and connection
cursorObject.close()
dataBase.close()

print('Database created successfully!')