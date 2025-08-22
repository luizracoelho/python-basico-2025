# Aula 5.3. Métodos básicos: append(), remove(), sort().
frutas = ["maçã", "banana", "laranja", "uva", "pera"]

# Adicionando um item à lista
frutas.append("kiwi")
print(f"\nApós append: {frutas}")

# Removendo um item da lista por chave
frutas.remove("banana")
print(f"\nApós remove: {frutas}")

# Removendo um item da lista por índice
frutas.pop(2)
print(f"\nApós pop: {frutas}")

# Modificando um item da lista
frutas[0] = "manga"
print(f"\nApós modificar: {frutas}")

# Invertendo a lista
frutas.reverse()
print(f"\nApós reverse: {frutas}")

# Ordenando a lista
frutas.sort()
print(f"\nApós sort: {frutas}")

# Ordenando a lista de forma reverse
frutas.sort(reverse=True)
print(f"\nApós sort reverse: {frutas}")

# Convertendo a lista em uma string
frutas_str = ", ".join(frutas)
print(f"\nLista de frutas: {frutas_str}")

# Convertendo a string de volta em uma lista
frutas_lista = frutas_str.split(", ")
print(f"\nLista de frutas (a partir da string): {frutas_lista}")