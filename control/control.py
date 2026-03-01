def create_task():
    new_task = []
    try:
        print("Criando nova tarefa")
        new_task.append(str(input("Nome da tarefa: ")))
        str(input("Descrição da tarefa: "))
        int(input("Status da tarefa(0 para em aberto, 1 para concluido): "))
    except:
        print("Não foi possível criar a tarefa")