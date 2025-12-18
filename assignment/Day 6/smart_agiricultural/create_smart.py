import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'smart_iotdb',
    use_pure = True
)

id =int(input("Enter the id: "))
sensor_id =int(input("Enter the sensor_id: "))
moisture_level =float(input("Enter the moisture_level: "))

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

query = f"INSERT INTO soil_moisture VALUES ({id},{sensor_id},{moisture_level},'{timestamp}')"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()

print("Inserted successfully")


