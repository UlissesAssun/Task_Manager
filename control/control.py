def create_task():
    title = None
    description = None
    status = None

    try:
        print("Criando nova tarefa")
        title = str(input("Nome da tarefa: "))
        description = str(input("Descrição da tarefa: "))
        status = int(input("Status da tarefa(0 para em aberto, 1 para concluido): "))
    except:
        print("Não foi possível criar a tarefa")

        return title, description, status