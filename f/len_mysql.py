import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',           # or 127.0.0.1
        user='root',                # your MySQL username
        password='uUkol87g65tr@W3*h21y',   # your MySQL password
        database='laptop_data'    # make sure this exists
    )

    if conn.is_connected():
        print("✅ Successfully connected to MySQL database")
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        for table in cursor.fetchall():
            print("📄", table)
        cursor.close()
        conn.close()
    else:
        print("❌ Could not connect.")

except Error as e:
    print("❌ Error while connecting to MySQL:", e)