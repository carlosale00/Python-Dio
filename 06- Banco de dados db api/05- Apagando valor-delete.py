import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conect = sqlite3.connect(ROOT/"meu_db.db")

# instanciândo o cursor que irá executar instruções SQL
cursor = conect.cursor()

# função para apagar linha com determinado valor de id


def apagar_valores(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?;", data)
    conexao.commit()
    print(f"id {data[0]} excluida com sucesso")


apagar_valores(conect, cursor, 2)

# fechando conexão com BD
conect.close()
