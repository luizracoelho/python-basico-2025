# Aula 8.1 - O que são funções e módulos

## O que são funções?

Funções são blocos de código que executam uma tarefa específica e podem ser reutilizados em diferentes partes do programa.  
Elas ajudam a **organizar o código**, evitar repetição e melhorar a legibilidade.

### Estrutura básica de uma função

```python
def nome_da_funcao(parametros):
    # bloco de código
    return resultado
```

- **def**: palavra-chave usada para declarar a função
- **nome_da_funcao**: identificador escolhido para a função
- **parametros**: valores que a função pode receber _(opcional)_
- **return**: usado para retornar um valor _(opcional)_

Exemplo prático
```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))
# Saída: Olá, Maria!
```

Funções sem retorno
```python
def mostrar_mensagem():
    print("Bem-vindo ao curso de Python!")

mostrar_mensagem()
# Saída: Bem-vindo ao curso de Python!
```

Funções com múltiplos parâmetros
```python
def somar(a, b):
    return a + b

print(somar(5, 3))
# Saída: 8
```

## O que são módulos?

Além dos módulos já incluídos no Python e os que podem ser instalados de terceiros, também é possível **criar seus próprios módulos (arquivos .py)** e reutilizá-los em outros projetos.

### Criando um módulo simples

1. Crie um arquivo chamado `meu_modulo.py` com o seguinte conteúdo:

```python
def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo."
```

2. Agora, em outro arquivo Python (por exemplo, app.py), você pode importar e usar essa função:
```python
import meu_modulo

print(meu_modulo.saudacao("Maria"))
# Saída: Olá, Maria! Seja bem-vindo.
```

Importando apenas funções específicas
```python
from meu_modulo import saudacao

print(saudacao("João"))
# Saída: Olá, João! Seja bem-vindo.
```
Renomeando módulos ou funções ao importar
```python
import meu_modulo as mm

print(mm.saudacao("Ana"))
# Saída: Olá, Ana! Seja bem-vindo.
```