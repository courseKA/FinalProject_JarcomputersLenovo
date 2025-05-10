import mysql.connector
from mysql.connector import Error

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='uUkol87g65tr@W3*h21y',
    database='laptop_data'
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS laptops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name TEXT,
    price VARCHAR(255),
    screen_size_cm VARCHAR(50)
)
""")

# Insert data
for item in laptop_data:
    cursor.execute("""
    INSERT INTO laptops (product_name, price, screen_size_cm)
    VALUES (%s, %s, %s)
    """, (item['Product Name'], item['Price'], item['Screen Size (cm)']))

conn.commit()
cursor.close()
conn.close()

print("✅ Data also saved to MySQL.")