import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'iot_data',
    use_pure = True
)
id = int(input("Enter the id: "))
temp = float(input("Enter the temperature"))
humidity = float(input("Enter the humidity"))

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

query = f"INSERT INTO sensor_readings VALUES ({id},{temp},{humidity},'{timestamp}')"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()

print("Inserted successfully")
