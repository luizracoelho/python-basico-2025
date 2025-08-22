# Aula 6.1 – O que são Dicionários (Dados em Pares Chave-Valor)

## O que são dicionários
- Dicionários são **coleções de dados**, mas ao invés de usar índices numéricos, eles usam **pares chave-valor**.  
- Cada **chave** é única e está associada a um **valor**.  
- Valores podem ser de qualquer tipo: números, strings, listas, outras estruturas, etc.  

```python
# Exemplo de dicionário
aluno = {
    "nome": "Maria",
    "idade": 20,
    "curso": "Python"
}
```

## Acessando valores
- Para acessar um valor, usamos a chave correspondente:

```python
print(aluno["nome"])   # "Maria"
print(aluno["idade"])  # 20
```

## Modificando valores
- Podemos alterar um valor usando a chave:

```python
aluno["idade"] = 21
print(aluno["idade"])  # 21
```

## Adicionando e removendo itens
- Adicionar um novo par chave-valor:

```python
aluno["email"] = "maria@email.com"
```
- Remover um item:

```python
del aluno["curso"]
```

- Operações básicas
    - len(dicionario) → quantidade de pares chave-valor
    - dicionario.keys() → lista de chaves
    - dicionario.values() → lista de valores
    - dicionario.items() → lista de pares (chave, valor)

```python
print(len(aluno))
print(aluno.keys())
print(aluno.values())
print(aluno.items())
```