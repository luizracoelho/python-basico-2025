# Aula 7.1 – O que são Estruturas de Decisão e Repetição

## Estruturas de decisão
- Estruturas de decisão permitem que o programa **escolha entre diferentes caminhos** dependendo de condições.  
- As principais em Python:
  - `if` – se a condição for verdadeira, executa um bloco de código
  - `elif` – se a condição anterior for falsa, testa outra condição
  - `else` – executa um bloco se todas as condições anteriores forem falsas

```python
idade = 18
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
```

### Operadores de comparação
- Usados para tomar decisões:

```bash
==  : igual
!=  : diferente
>   : maior que
<   : menor que
>=  : maior ou igual
<=  : menor ou igual
```

### Operadores lógicos
- Permitem combinar condições:

```bash
and  : e
or   : ou
not  : não
```
### Exemplo de uso de operadores de comparação e lógicos:
```python
idade = 20
curso = "Python"
if idade >= 18 and curso == "Python":
    print("Pode participar do curso")
```

## Estruturas de repetição
- Permitem que um bloco de código se repita várias vezes enquanto uma condição for verdadeira.

### Loop for
- Percorre elementos de uma sequência (lista, string, range):

```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

### Loop while
- Executa enquanto a condição for verdadeira:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### Controle de fluxo em loops
```bash
break → interrompe o loop
continue → pula para a próxima iteração
```

```python
for i in range(5):
    if i == 3:
        break
    print(i)  # Saída: 0 1 2

for i in range(5):
    if i == 3:
        continue
    print(i)  # Saída: 0 1 2 4
```