import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conect = sqlite3.connect(ROOT/"meu_db.db")

# instanciândo o cursor que irá executar instruções SQL
cursor = conect.cursor()

# salvando os dados que serão inseridos em uma tupla
data = ("Carlos", "dasilvacarlosale00@gmail.com")

# executando o comando sql
cursor.execute("INSERT INTO clientes (nome, email) VALUES(?,?);", data)

# confirmando a transação
conect.commit()

# fechando conexão com BD
conect.close()
