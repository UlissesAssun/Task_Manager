from control.control import create_task

while True:
    choice = int(input(""" ---Olá, seja bem vindo ao Task Manger---
              ------Escolha uma das opções abaixo-----
              -----1:Criar Tarefa.--------------------
              -----2:Listar Tarefas.------------------
              -----3:Editar Status da Tarefa.---------
              -----4:Deletar Tarefa.------------------
              -----5:Sair.----------------------------
          """))

    match choice:

        case 1:
            create_task()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            pass


