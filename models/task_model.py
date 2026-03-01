import sqlite3 as sq
from models.database import DB_PATH
from control.control import create_task

task_info = []

def db_create_task(task_info):
    'Cria a tarefa no banco de dados'

    with sq.connect(DB_PATH) as con:
        cur = con.cursor()

        cur.execute("""
        INSERT INTO tasks ( title, description, status
        VALUES(?,?,?)""", (task_info[0], task_info[1], task_info[2]))

    input("Tarefa criada com sucesso!(Prescione qualque tecla para continuar.)")
