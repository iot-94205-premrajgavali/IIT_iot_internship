import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'iot_data',
    use_pure = True
)

temp = float(input("Enter the temp : "))
humi = float(input("Enter the humidity : "))

query = f"update sensor_readings SET temp = {temp}where humidity = {humi};"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()

print("updated sucessfully")