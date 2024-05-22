import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conect = sqlite3.connect(ROOT/"meu_db.db")

# instanciândo o cursor que irá executar instruções SQL
cursor = conect.cursor()

# salvando os dados que serão inseridos em uma tupla
data = ("Marco", 1)

# executando o comando sql , que altera o nome caso id seja de tal valor
cursor.execute(
    "UPDATE clientes SET nome = ? WHERE id = ?;", data)

# confirmando a transação
conect.commit()


# usando uma funçao para atualização do BD
def atualizar_bd(conexao, cursor, nome, id,):
    data = (nome, id)
    cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?;", data)
    conexao.commit()


atualizar_bd(conect, cursor, "Carlos", 1)


# fechando conexão com BD
conect.close()
