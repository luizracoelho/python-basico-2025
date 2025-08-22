# Aula 3.2. Concatenar (juntar) textos.

# Concatenar textos significa juntar duas ou mais strings em uma única string.

# Concatenando strings
texto1 = "Olá"
texto2 = "mundo!"
texto_concatenado = texto1 + ", " + texto2

print(texto_concatenado)

# Concatenando diferentes tipos de dados
# Necessário conversão para string
nome = "João"
numero = 42

texto_com_numero = nome + " tem " + str(numero) + " anos de idade"
print(texto_com_numero)
