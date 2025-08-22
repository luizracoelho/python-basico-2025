# Criar uma lista de compras básica inicialmente com 3 itens, remover o primeiro item, substituir o valor do último e por fim adicionar mais 2 novos itens.
# Imprima o antes e depois da lista

lista_compras = ["maçã", "banana", "laranja"]
print(lista_compras)

# Remover o primeiro item
lista_compras.pop(0)

# Substituir o valor do último item
lista_compras[-1] = "abacaxi"

# Adicionar mais 2 novos itens
lista_compras.append("uva")
lista_compras.append("manga")

print("Lista de Compras Atualizada:")
print(lista_compras)