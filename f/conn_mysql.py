import mysql.connector

# Database connection parameters
cnx_kwargs = {
    'host': 'localhost',     # MySQL server address
    'user': 'root',          # MySQL username
    'password': 'uUkol87g65tr@W3*h21y',  # MySQL password
    'database': 'laptop_data'    # Ensure this is the correct database name
}

# Establish the connection
try:
    connection = mysql.connector.connect(**cnx_kwargs)
    print("Successfully connected to the database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")