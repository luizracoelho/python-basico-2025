# Criar uma menu simples com repetição, onde o usuário pode escolher opções até sair do programa. Se o número informado for inferior ou igual a 0 deve retornar uma mensagem falando que o valor é muito baixo, caso o valor seja superior a 5 deve-se mostrar uma mensgaem falando que o valor é muito alto. Se a opção escolhida for 5, encerra-se o programa, caso contrário permanece a execução do loop.

while True:
    print("\nMenu:")
    print("1. Adicionar Aluno")
    print("2. Remover Aluno")
    print("3. Listar Alunos")
    print("4. Encontrar Aluno")
    print("5. Sair")

    opcao = input("Escolha uma opção\n==================\n")

    if opcao.isdigit():
        opcao = int(opcao)
        if opcao <= 0:
            print("Valor muito baixo.")
        elif opcao > 5:
            print("Valor muito alto.")
        elif opcao == 5:
            print("Saindo...")
            break
    else:
        print("Opção inválida. Tente novamente.")
