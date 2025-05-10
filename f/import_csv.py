import csv
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="uUkol87g65tr@W3*h21y",
    database="laptop_data"
)
cursor = conn.cursor()

# Read the CSV file
with open(r'C:\Users\ksa\our_spider\jarcom1\jarcom1\spiders\jar_lenovo_laptops.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        cursor.execute(
            "INSERT INTO laptops (id, name, brand, price, release_date) VALUES (%s, %s, %s, %s, %s)", 
            row
        )

# Commit and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data imported successfully")