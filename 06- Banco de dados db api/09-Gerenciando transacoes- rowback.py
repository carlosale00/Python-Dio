import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conect = sqlite3.connect(ROOT/"meu_db.db")

# instânciândo o cursor que irá executar instruções SQL
cursor = conect.cursor()

# caso
try:
    dados = ("zelinda", "zelinda@gmail.com")
    # executando o comando sql
    cursor.execute("INSERT INTO clientes(nome, email) VALUES(?,?);", dados)

    # dados com erros , ID ja existe
    dados = (1, "teste", "teste@gmail.com")
    # executando o comando sql
    cursor.execute(
        "INSERT INTO clientes(id,nome, email) VALUES(?,?,?);", dados)
    conect.commit()

except Exception as e:
    print(f"nao foi possivel concluir a operação {e}")
    conect.rollback()
    conect.close()


conect.close()
