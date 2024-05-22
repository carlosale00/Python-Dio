import sqlite3
from pathlib import Path

# caminho absuluto da nossa pasta
ROOT = Path(__file__).parent

# caso o BD não exista , sera criado um e conectado
conect = sqlite3.connect(ROOT/"meu_db.db")

# fechando a conexão com o BD
conect.close()
