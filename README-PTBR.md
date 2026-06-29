# pyllo_greeting

Uma aplicação CLI simples criada para estudar métodos de distribuição de aplicativos Python.

## Instalação

> ⚠️ Você precisa ter o Python instalado para usar esta aplicação.

1. Crie um ambiente virtual:

``` sh
python -m venv .venv  # Windows
python3 -m venv .venv # MacOS e Linux
```

2. Ative o ambiente:

``` sh
.venv\Scripts\activate    # Windows
source .venv/bin/activate # MacOS e Linux
```

3. Instale o projeto:

``` sh
pip install pyllo_greeting
```

4. Use o CLI:

``` sh
pyllo
# Saída: Hello there
```

### Opções

#### Nome e Tons

- É possível passar um nome/palavra para receber a saudação do app:

``` sh
pyllo John
# Hello there, John
```

``` sh
pyllo everyone
# Hello there, everyone
```

> Esse argumento é uma string, logo, caso haja espaços, deve ser passado entre aspas:

``` sh
pyllo "Sergio and Sara"
# Hello there, Sergio and Sara
```

- Além disso, também há a possibilidade de informar um tom. O tom padrão é o "normal":

1. `Normal/Padrão`:

``` sh
pyllo Alice
# Hello there, Alice
```

2. `Rápido (Quick)`:

``` sh
pyllo Theresa --quick
# Hi, Theresa

pyllo Matthew -q
# Hi, Matthew
```

3. `Elegante (Fancy)`:

``` sh
pyllo Leticia --fancy
# Greetings. It is truly a pleasure to acknowledge your existence, Leticia

pyllo Beatrice -f
# Greetings. It is truly a pleasure to acknowledge your existence, Beatrice
```

#### Random Greet

Ao usar o programa com a flag `--random | -r`, o CLI irá exibir uma frase de cumprimento aleatória.  
Essa frase pode ser uma das padrões (normal, rápida e elegante) ou uma completamente diferente.

``` sh
pyllo Antony --random
# Output: System check complete. Welcome, Antony.

pyllo Mary --random
# Output: Greetings, Mary.

pyllo Mark --random
# Output: What's up, Mark?
```

#### Meta Opções

Atualmente existem duas opções `meta`:

1. `Versão do App (--version | -v)`:

``` sh
pyllo -v
# 1.1.2
```

2. `Créditos do App (--credits | -c)`:

``` sh
pyllo -c
# Project created by:
#         João Antônio

# Author's GitHub:
#         https://github.com/joao-antonio-la

# Project's Repository:
#         https://github.com/joao-antonio-la/pyllo
```