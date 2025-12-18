import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'iot_data',
    use_pure = True
)

query = f'select * from sensor_readings;'

cursor = connection.cursor()
cursor.execute(query)
row =cursor.fetchall()
for row in row:
    print(row)

cursor.close()
connection.close()

print("fetched all data sucessfully")


