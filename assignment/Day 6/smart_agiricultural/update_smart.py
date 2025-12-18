import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'smart_iotdb',
    use_pure = True
)


id = int(input("Enter the id : "))
mois = float(input("Enter the moisture_level: "))


query = f"update soil_moisture SET moisture_level = {mois} WHERE id = {id} ;"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()

print("updated sucessfully")