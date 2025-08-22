# Aula 7.2. Estruturas de decisão:
# if, elif, else
# Comparações (==, !=, >, <, >=, <=)
# Operadores lógicos (and, or, not)

# Estrutura de decisão
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

# Comparações
if idade == 18:
    print("Você acabou de se tornar um adulto.")
elif idade != 18:
    print("Você não tem 18 anos.")

if idade == 18:
    print("Você tem 18 anos.")
else:
    print("Você não tem 18 anos.")

# Operadores lógicos
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")