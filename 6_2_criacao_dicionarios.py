# Aula 6.1. O que são dicionários (dados em pares chave-valor).

# Criando um dicionário
cliente = {
    "nome": "João",
    "idade": 30,
    "email": "joao@example.com",
    "possuiSaldo": True
}
print(f"Cliente: {cliente}")

# Acessando valores do dicionário
print(cliente['nome'])
print(cliente['idade'])
print(cliente['email'])
print(cliente['possuiSaldo'])