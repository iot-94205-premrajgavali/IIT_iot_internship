import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'smart_iotdb',
    use_pure = True
)

start = int(input("Enter the moisture_level start range: "))
end = int(input("Enter the moisture_level end range: "))

query = f'select * from soil_moisture WHERE moisture_level BETWEEN {start} and {end};'

cursor = connection.cursor()
cursor.execute(query)

row = cursor.fetchall()
for row in row:
    print(row) 
    
cursor.close()
connection.close()

print("range successfully displayed")

