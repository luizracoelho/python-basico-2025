# Aula 5.1 – O que são Listas (Coleções de Dados)

## O que são listas
- Listas são **coleções de dados**, que podem armazenar **vários valores em uma única variável**.  
- Os valores podem ser de **tipos diferentes**: números, strings, booleanos, outras listas, etc.  
- As listas são **mutáveis**, ou seja, podemos alterar seus elementos depois de criadas.  

```python
# Exemplo de lista
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mix = ["Python", 10, True]
```

## Criando listas
- Listas podem ser criadas usando colchetes [] e separando os elementos por vírgulas:

```python
lista_vazia = []
cores = ["vermelho", "verde", "azul"]
```

## Acessando elementos
- Cada elemento da lista possui um índice, que começa em 0.  
- Podemos acessar um elemento pelo seu índice:

```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # "maçã"
print(frutas[2])  # "laranja"
```

## Modificando elementos
- Podemos alterar valores da lista usando o índice:

```python
frutas[1] = "abacaxi"
print(frutas)  # ["maçã", "abacaxi", "laranja"]
```

## Operações básicas com listas
- Adicionar elementos: append()
- Remover elementos: remove() ou pop()
- Ver tamanho: len()

```python
frutas.append("manga")
frutas.remove("maçã")
print(len(frutas))  # tamanho da lista
```