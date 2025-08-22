# Aula 8.3. Criação e importação de módulos próprios.
# Arquivo principal

import meu_modulo as mm

mm.saudacao("João")

local_execucao = mm.obter_local_execucao()

resultado = mm.soma(5, 3)
print(f"O resultado da soma é: {resultado}")

mm.agora()

print(local_execucao)