import sqlite3

# Let's connect with the database
connection = sqlite3.connect("bank.db")

# Create a cursor to interact (CRUD)
cursor = connection.cursor()

# Write query to create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        acnum TEXT NOT NULL,
        actype TEXT NOT NULL,
        owname TEXT NOT NULL,
        branch TEXT NOT NULL,
        gender TEXT NOT NULL,
        balance TEXT NOT NULL
    )
''')

# Commit this to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("Table created successfully.")
