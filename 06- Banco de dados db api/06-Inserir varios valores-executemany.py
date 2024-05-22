import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conect = sqlite3.connect(ROOT/"meu_db.db")

# instanciândo o cursor que irá executar instruções SQL
cursor = conect.cursor()

# funçaõ para inserir varios valores no BD


def inserir_valores(conexao, cursor, dados):
    cursor.executemany(
        "INSERT INTO clientes(nome, email) VALUES(?,?);", dados)
    conexao.commit()


# dados que serão inseridos
dados = [
    ("amauri", "amauri@gamil"),
    ("marcos", "marcos@gmail.com")
]

inserir_valores(conect, cursor, dados)

# fechando conexão com BD
conect.close()
