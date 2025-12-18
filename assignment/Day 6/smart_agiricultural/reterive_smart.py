import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'smart_iotdb',
    use_pure = True
)

query = f'SELECT * FROM soil_moisture;'

cursor = connection.cursor()
cursor.execute(query)

row = cursor.fetchall()
for row in row:
    print(row)
cursor.close()
connection.close()

print("fetched all data sucessfully")
