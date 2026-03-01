#Criação do banco de dados definindo todos os atributos necessários para a criação de uma tarefa

import sqlite3 as sq

DB_PATH = 'database.db'

def init_database():
    """Cria a tabela `tasks` se ainda não existir."""
    with sq.connect(DB_PATH) as con:
        cur = con.cursor()
        # Estrutura da tabela com validações mínimas via NOT NULL/DEFAULT
        cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL DEFAULT '',
                    description TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        """)