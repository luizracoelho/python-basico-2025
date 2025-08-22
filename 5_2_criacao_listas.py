# Aula 5.2. Criando listas e acessando elementos.

# Criando uma lista
frutas = ["maçã", "banana", "laranja", "uva"]

# Acessando elementos da lista
print(frutas[0])  
print(frutas[1])  
print(frutas[2]) 
print(frutas[3])  

# Acessando o primeiro item da lista
print(f"\nPrimeiro item: {frutas[0]}")

# Acessando o último item da lista
print(f"\nÚltimo item: {frutas[-1]}")

# Acessando os 3 primeiros itens da lista
print(f"\nTrês primeiros itens: {frutas[:3]}")

# Acessando os 3 últimos itens da lista
print(f"\nTrês últimos itens: {frutas[-3:]}")

# Acessando os 2 itens do meio da lista
print(f"\nDois itens do meio: {frutas[1:3]}")