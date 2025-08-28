# Python Básico 2025

## Instalação
- [Python](https://www.python.org/downloads)
- [Visual Studio Code](https://code.visualstudio.com/Download)

Para validar a instalação do Python, você pode rodar o seguinte comando:
```bash
python --version
```
_Ele deve retornar algo semelhante a isto:_ **Python 3.11.9**

## Criação de Ambiente Virtual
**Etapa 1)** Via terminal, acessar a pasta raiz do projeto, como por exemplo:
```bash
cd meu-projeto-python
```

**Etapa 2)** Rodamos o seguinte comando para criar um ambiente virtual:
```bash
python -m venv .venv
```
<small>_Funciona somente com Python 3.3 ou superior_</small>

**Etapa 3)** Agora precisaremos ativar nosso ambiente virtual:

> **Linux/MacOS**
>```bash
> source .venv/bin/activate
> ```

> **Windows**
> ```bash
> .\.venv\Scripts\Activate
> ```

O ideal é trabalharmos com um **venv** por projeto. Caso precisarmos trabalhar em outro projeto, devemos primeiramente desativar o ambiente virtual que estamos executando, para isso, basta digitar o seguinte comando:
```bash
deactivate
```

## Seções
### Módulo 1 - Introdução ao Python
- **Aula 1.1.** O que é Python e onde ele é usado?
- **Aula 1.2.** Primeiro programa em Python: **Olá Mundo!**
- **Aula 1.3.** Segundo programa em Python: **Olá Fulano!**

### Módulo 2 - Variáveis e Tipos de Dados
- **Aula 2.1.** O que são variáveis e como armazenam informações.
- **Aula 2.2.** Tipos básicos: números, textos (strings), booleanos.
- **Aula 2.3.** Convenções de nomes de variáveis.

#### Desafio:
> Criar variáveis com informações pessoais (nome, idade, cidade).

### Módulo 3 - Strings (Textos)
- **Aula 3.1.** O que são strings.
- **Aula 3.2.** Concatenar (juntar) textos.
- **Aula 3.3.** Formatação simples (f-strings).
- **Aula 3.4.** Métodos básicos: upper(), lower(), strip(), replace().

#### Desafio:
> Criar uma saudação personalizada com o nome do usuário e manipular o texto.

### Módulo 4 - Números e Operações
- **Aula 4.1.** O que são tipos numéricos: inteiro e decimal.
- **Aula 4.2.** Operações básicas: soma, subtração, multiplicação, divisão.
- **Aula 4.3.** Uso do round() e type().

#### Desafio:
> Criar uma mini-calculadora que ao receber 2 números retorna o resultado de todas as operações.

### Módulo 5 - Listas
- **Aula 5.1.** O que são listas (coleções de dados).
- **Aula 5.2.** Criando listas e acessando elementos.
- **Aula 5.3.** Métodos básicos: append(), remove(), sort().

#### Desafio:
> Criar uma lista de compras básica inicialmente com 3 itens, remover o primeiro item, substituir o valor do último e por fim adicionar mais 2 novos itens.

### Módulo 6 - Dicionários
- **Aula 6.1.** O que são dicionários (dados em pares chave-valor).
- **Aula 6.2.** Criando e acessando valores.
- **Aula 6.3.** Adicionar, modificar e remover chaves.
- **Aula 6.4.** Métodos úteis: keys(), values(), items()

#### Desafio:
> Criar uma ficha de cadastro de aluno com nome, idade e curso. Criar uma lista de fichas e adicionar 3 fichas a ela. Imprima a lista completa e depois somente os valores da lista, ignorando as chaves.

### Módulo 7 - Estruturas de Decisão e Repetição
- **Aula 7.1.** O que são estruturas de decisão e de repetição. 
- **Aula 7.2.** Estruturas de decisão: 
    - if, elif, else
    - Comparações (==, !=, >, <, >=, <=)
    - Operadores lógicos (and, or, not)
- **Aula 7.3.** Estruturas de repetição
    - for (percorrer listas, range)
    - while (repetir enquanto uma condição for verdadeira)
- **Aula 7.4.** Controle de fluxo
    - break (interrompe o loop)
    - continue (pula para a próxima iteração)

#### Desafio:
> Criar uma menu simples com repetição, onde o usuário pode escolher opções até sair do programa. Se o número informado for inferior ou igual a 0 deve retornar uma mensagem falando que o valor é muito baixo, caso o valor seja superior a 5 deve-se mostrar uma mensgaem falando que o valor é muito alto. Se a opção escolhida for 5, encerra-se o programa, caso contrário permanece a execução do loop.

### Módulo 8 - Declaração de funções e importação de libs próprias
- **Aula 8.1.** O que são funções e módulos.
- **Aula 8.2.** Declarando e utilizando funções.
- **Aula 8.3.** Criação e importação de módulos próprios.

#### Desafio:
> Criar um arquivo apartado com funções básicas de calculadora e no arquivo principal, pedir para o usuário informar uma operação básica. Seu programa precisa identificar a operação para chamar a função correta do arquivo auxiliar passando os 2 números como parâmetro.

### Módulo 9 - Projeto Final
#### Desafio Final: Sistema de Cadastro de Alunos

> Você deve criar um **sistema simples de cadastro de > alunos**, que será executado no terminal.  
> O programa deve rodar em loop (`while True`) e > apresentar um **menu de opções** para o usuário > interagir.
> 
> ---
> 
> #### Requisitos:
> 
> 1. **Estrutura de dados:**
>    - Os alunos devem ser armazenados em uma **lista de > dicionários**.
>    - Cada dicionário deve conter as seguintes chaves:
>      - `nome`
>      - `idade`
>      - `curso`
> 
> 2. **Menu principal:**
>    O programa deve exibir as seguintes opções:
>    - `1` - Adicionar aluno
>    - `2` - Remover aluno
>    - `3` - Alterar dados de um aluno
>    - `4` - Listar todos os alunos
>    - `9` - Sair do programa
> 
> 3. **Funcionalidades:**
>    - **Adicionar aluno**: pedir nome, idade e curso e > salvar na lista.
>    - **Remover aluno**: pedir o nome do aluno e remover > da lista (se existir).
>    - **Alterar dados**: permitir atualizar a idade ou > curso de um aluno já cadastrado.
>    - **Listar alunos**: exibir todos os alunos > cadastrados de forma organizada.
>    - **Sair**: encerrar o programa.
> 
> 4. **Funções:**
>    - Organize seu código em **funções** para cada > funcionalidade (ex.: `adicionar_aluno`, > `remover_aluno`, `listar_alunos`, etc).
> 
> 5. **Extras (opcional):**
>    - Validar se o aluno já existe antes de adicionar.
>    - Não permitir remover ou alterar se o aluno não > existir.
>    - Criar um módulo separado chamado `alunos.py` com > todas as funções, e no arquivo principal apenas > importar e chamar essas funções.
> 
> ---
> 
> #### Exemplo de execução esperada:
> 
> ==== Sistema de Cadastro de Alunos ====  
> 1 - Adicionar aluno  
> 2 - Remover aluno  
> 3 - Alterar aluno  
> 4 - Listar alunos  
> 9 - Sair  
> Escolha uma opção: 1
> 
> Digite o nome do aluno: Maria  
> Digite a idade do aluno: 22  
> Digite o curso do aluno: Engenharia
> 
> Aluno adicionado com sucesso!
> 
> ---
> 
> ✅ **Objetivo**: Este desafio final vai consolidar todos > os conceitos aprendidos:
> - Variáveis, strings e números  
> - Listas e dicionários  
> - Estruturas de decisão e repetição  
> - Funções e módulos  
