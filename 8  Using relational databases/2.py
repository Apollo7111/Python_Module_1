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
data = {}
list = []
areaCode = input('Please input area code of the airport: ')
sql = f"SELECT type, name FROM airports WHERE iso_country='{areaCode}'"
try:
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    for row in sorted(result):
        if(row[0] not in data.keys()):
            # list.append({row[0]: row[1]})
            data.update({row[0]: row[1]})
        # print(row[0])
        # print(data[row[0]])
        else:
            data[row[0]] += ', ' + row[1]
            # data[row[0]] = data[row[0]].values(), row[1]
except mysql.connector.Error as e:
    print(f"Error creating table: {e}")
print(f'{areaCode} has: ')
for item in data:
    print(f'\n{item}: {data[item]}')
# for record in data:
#     print(f'{record}: {data[record]}')


