import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='world0000000000000000000000000000000000000000000000',
    user='root',
    password='123456789',

)
if conexao.is_connected():
    db_info = conexao.get_server_info()
    print('Conexão bem sucedida',db_info)
    cursor = conexao.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print('Conexão de BD', linha)

if conexao.is_connected():
    cursor.close()
    conexao.cursor()
    print("Finalizado conecxão")
