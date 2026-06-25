# pyllo

Uma aplicação CLI simples criada para estudar métodos de distribuição de aplicativos Python.

## Instalação

> ⚠️ Você precisa ter o Python instalado para usar esta aplicação.

1. Clone o repositório:

``` sh
git clone https://github.com/joao-antonio-la/pyllo.git
```

- Após clonar o repositório, você está pronto para usar a aplicação.

## Como Usar

Com a aplicação localmente na sua máquina, você pode utilizá-la seguindo os passos abaixo:

1. Entre na pasta do projeto: 

``` sh
cd pyllo
```

2. Crie um ambiente virtual:

``` sh
python -m venv .venv # Windows
python3 -m venv .venv # MacOS e Linux
```

3. Ative o ambiente:

``` sh
.venv\Scripts\activate    # Windows
source .venv/bin/activate # MacOS e Linux
```

4. Instale o projeto localmente:

``` sh
pip install .
```

5. Use o CLI:

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

#### Meta Opções

Atualmente existem duas opções `meta`:

1. `Versão do App (--version | -v)`:

``` sh
pyllo -v
# 0.1.0
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