import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conect = sqlite3.connect(ROOT/"meu_db.db")

# instanciândo o cursor que irá executar instruções SQL
cursor = conect.cursor()

# fazendo a pesquisa e retornando o valor unico no terminal
cursor.execute("SELECT * FROM clientes WHERE id = 1 ")
resultado = cursor.fetchone()
print(resultado)

# fazendo a pesquisa e retornando todos os valores no terminal
cursor.execute("SELECT * FROM clientes")
resultado = cursor.fetchall()
print(resultado)

cursor.execute("SELECT * FROM clientes")
resultado = cursor.fetchmany()
print(resultado)


# fechando conexão com BD
conect.close()
