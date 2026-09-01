
tarefas = []

while True:
    
    print("\n--- MENU DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Mostrar tarefas")
    print("0 - Sair")
    
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nova_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")
        
    elif opcao == "2":
        if len(tarefas) == 0:
            print("A lista está vazia. Não há nada para remover.")
        else:
            tarefa_remover = input("Digite o nome da tarefa que deseja remover: ")
            if tarefa_remover in tarefas:
                tarefas.remove(tarefa_remover)
                print(f"Tarefa '{tarefa_remover}' removida com sucesso!")
            else:
                print("Tarefa não encontrada na lista.")
                
    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada no momento.")
        else:
            print("\nSua lista de tarefas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa}")
                
    elif opcao == "0":
        print("Saindo do programa... Até mais!")
        break
        
    else:
        print("Opção inválida! Por favor, escolha um número do menu.")
