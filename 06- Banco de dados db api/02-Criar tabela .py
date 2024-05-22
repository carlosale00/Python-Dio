import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conect = sqlite3.connect(ROOT/"meu_db.db")

# instanciândo o cursor que irá executar instruções SQL
cursor = conect.cursor()

# criando uma tabela no BD
cursor.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, \
nome VARCHAR(100), email VARCHAR(150))")


conect.close()
