# Aula 3.4. Métodos básicos: upper(), lower(), strip(), replace().
texto = "   Olá, Mundo!   "

# upper(): Converte todo o texto para maiúsculas
texto_em_maiusculo = texto.upper()
print(texto_em_maiusculo)

# lower(): Converte todo o texto para minúsculas
texto_em_minusculo = texto.lower()
print(texto_em_minusculo)

# strip(): Remove espaços em branco do início e do fim
texto_sem_espacos = texto.strip()
print(texto_sem_espacos)

# replace(): Substitui uma parte do texto por outra
texto_substituido = texto.replace("Mundo", "Python")
print(texto_substituido)

# Verificar se uma string possui conteúdo numérico ou não
print(texto_sem_espacos.isdigit())
print("12345".isdigit())