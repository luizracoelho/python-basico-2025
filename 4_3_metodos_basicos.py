# Aula 4.3. Uso do round() e type().
numero = 5.6789
texto_int = "7"
texto_float = "6.98"

# round(): Arredonda um número
numero_arredondado = round(numero, 2)
print(f"Número arredondado: {numero_arredondado}")

# type(): Retorna o tipo de uma variável
tipo_numero = type(numero)
print(f"Tipo de número: {tipo_numero}")

# int(): Converte um valor para inteiro
numero_inteiro = int(texto_int)
print(f"Número inteiro: {numero_inteiro}")

# float(): Converte um valor para ponto flutuante
numero_float = float(texto_float)
print(f"Número float: {numero_float}")