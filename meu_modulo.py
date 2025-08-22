# Aula 8.3. Criação e importação de módulos próprios.
# Meu Módulo

from datetime import datetime

def agora():
    print("Horário de execução:", datetime.now().time())

def obter_local_execucao():
    return "Local de execução: " + __file__

def saudacao(nome):
    print(f"Olá, {nome}!")

def soma(a, b):
    return a + b
