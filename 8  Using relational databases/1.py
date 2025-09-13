import mysql.connector
try:
    connection = mysql.connector.connect(
             host='127.0.0.1',
             port= 3306,
             database='airport',
             user='root',
             password='',
             autocommit=True
             )
except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB: {e}")

icao = input('Please input ICAO code of the airport: ')
sql = f"SELECT name, municipality FROM airports WHERE ident='{icao}'"
try:
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
except mysql.connector.Error as e:
    print(f"Error creating table: {e}")


