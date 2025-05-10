import mysql.connector
import csv

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='uUkol87g65tr@W3*h21y',
    database='laptop_data'
)
cursor = conn.cursor()

# ✅ Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS lenovo_laptops (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(255),
        price DECIMAL(10, 2),
        screen_size_cm FLOAT
    )
""")

# ⚠️ Optional: clear old data
cursor.execute("DELETE FROM jar_lenovo_laptops")

# Load CSV
with open('C:/Users/ksa/our_spider/jarcom1/jarcom1/spiders/jar_lenovo_laptops.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        cursor.execute("""
            INSERT INTO jar_lenovo_laptops (product_name, price, screen_size_cm)
            VALUES (%s, %s, %s)
        """, (
            row['Product Name'],
            row['Price'],
            row['Screen Size (cm)']
        ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data successfully inserted into MySQL!")