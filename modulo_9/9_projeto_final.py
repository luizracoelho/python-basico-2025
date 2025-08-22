# Desafio Final: Sistema de Cadastro de Alunos
# Arquivo principal

import os
import time
from alunos import buscar_aluno, adicionar_aluno, remover_aluno, alterar_aluno, listar_alunos

index = 0

def limpar_tela():
    global index

    if (index > 0):
        time.sleep(1)
    
    os.system("cls" if os.name == "nt" else "clear")
    index += 1

def menu():
    limpar_tela()
    print("==== Sistema de Cadastro de Alunos ====")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Alterar aluno")
    print("4 - Listar alunos")
    print("9 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")
        adicionar_aluno(nome, idade, curso)

    elif opcao == "2":
        nome = input("Digite o nome do aluno a ser removido: ")
        remover_aluno(nome)

    elif opcao == "3":
        nome = input("Digite o nome do aluno que deseja alterar: ")
        aluno = buscar_aluno(nome)
    
        if aluno:  # só pede os novos dados se o aluno existir
            idade = input("Digite a nova idade (ou pressione Enter para não alterar): ")
            curso = input("Digite o novo curso (ou pressione Enter para não alterar): ")

            idade = int(idade) if idade.strip() else None
            curso = curso if curso.strip() else None

            alterar_aluno(nome, idade, curso)

    elif opcao == "4":
        listar_alunos()

    elif opcao == "9":
        print("👋 Saindo do programa. Até mais!")
        break

    else:
        print("⚠️ Opção inválida! Tente novamente.")
