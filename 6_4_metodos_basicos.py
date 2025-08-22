# Aula 6.4. Métodos úteis: keys(), values(), items()

cliente = {
    "nome": "João",
    "idade": 30,
    "email": "joao@example.com",
    "possuiSaldo": True
}

print(cliente.keys())
print(cliente.values())
print(cliente.items())

# A função items() retorna uma lista de tuplas, onde cada tupla contém uma chave e seu valor correspondente.
# - Tuplas são estruturas de dados que podem armazenar múltiplos itens em uma única variável.
# - Elas são imutáveis, o que significa que, uma vez criadas, não podem ser alteradas.
# - As tuplas são definidas usando parênteses, enquanto as listas usam colchetes.
# - As tuplas não são tão amplamente utilizadas quanto as listas, mas são úteis em situações onde a imutabilidade é desejada.

# Convertendo uma tupla em lista
lista_tupla = list(cliente.items())

print(lista_tupla)
print(lista_tupla[0])
print(lista_tupla[0][0])
print(lista_tupla[0][1])