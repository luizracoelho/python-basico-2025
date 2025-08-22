# Criar uma ficha de cadastro de aluno com nome, idade e curso. Criar uma lista de fichas e adicionar 3 fichas a ela. Imprima a lista completa e depois somente os valores da lista, ignorando as chaves.

ficha_aluno1 = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia"
}

ficha_aluno2 = {
    "nome": "Maria",
    "idade": 22,
    "curso": "Medicina"
}

ficha_aluno3 = {
    "nome": "Pedro",
    "idade": 21,
    "curso": "Arquitetura"
}

lista_fichas = [ficha_aluno1, ficha_aluno2, ficha_aluno3]

print("Lista de Fichas:")
print(lista_fichas)

print("Valores da primeira ficha:")
print(lista_fichas[0].values())
print(lista_fichas[1].values())
print(lista_fichas[2].values())