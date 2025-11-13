from flask import Flask, request
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


app = Flask(__name__)
@app.route(f'/airport/<icao>')
def prime(icao):
    name = ''
    location = ''
    airport = None
    sql = f"SELECT name, municipality FROM airports WHERE ident='{icao}'"
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        airport = result
    except mysql.connector.Error as e:
        print(f"Error creating table: {e}")
    response = {
        "ICAO": icao,
        "Name": airport[0][0],
        "Location": airport[0][1]
    }
    return response
if __name__ == '__main__':
    # app.run(use_reloader=True, host='127.0.0.1', port=3000)
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
