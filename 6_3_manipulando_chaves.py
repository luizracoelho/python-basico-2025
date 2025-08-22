# Aula 6.3. Adicionar, modificar e remover chaves.

cliente = {
    "nome": "João",
    "idade": 30,
    "email": "joao@example.com",
    "possuiSaldo": True
}

# Adicionando um item ao dicionário
cliente['telefone'] = "1234-5678"
print(cliente)

# Modificando um item do dicionário
cliente['email'] = "joao.novo@example.com"
print(cliente)

# Removendo um item do dicionário
del cliente['idade']
print(cliente)
