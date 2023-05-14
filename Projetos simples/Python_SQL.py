import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456789',
    database='crudpy',
)

cursor = conexao.cursor()


cursor.close()
conexao.cursor()
