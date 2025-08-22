# Aula 8.2. Declarando e utilizando funções.

from datetime import datetime

def agora():
    print("Horário de execução:", datetime.now().time())

def obter_local_execucao():
    return "Local de execução: " + __file__

def saudacao(nome):
    print(f"Olá, {nome}!")

def soma(a, b):
    return a + b

# Utilizando as funções
saudacao("João")

local_execucao = obter_local_execucao()

resultado = soma(5, 3)
print(f"O resultado da soma é: {resultado}")

agora()

print(local_execucao)
