import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conect = sqlite3.connect(ROOT/"meu_db.db")

# instanciândo o cursor que irá executar instruções SQL
cursor = conect.cursor()
cursor.row_factory = sqlite3.Row


cursor.execute("SELECT * FROM clientes WHERE id = 1 ")
resultado = cursor.fetchone()

# retornando o valor em uma lista
print(list(resultado))

# retornando o valor em um dicionario
print(dict(resultado))

# valores acessador pelo seu indice
print(resultado[0], resultado[1], resultado[2])


# # fazendo a pesquisa e retornando todos os valores no terminal
# cursor.execute("SELECT * FROM clientes")
# resultado = cursor.fetchall()
# print(resultado)

# cursor.execute("SELECT * FROM clientes")
# resultado = cursor.fetchmany()
# print(resultado)

# fechando conexão com BD
conect.close()
