# pyllo_greeting

Simple CLI application created for studying Python apps distribution methods.

## Installation

> ⚠️ You must have python installed to use this application.

1. Create a virtual environment:

``` sh
python -m venv .venv  # Windows
python3 -m venv .venv # MacOS and Linux
```

2. Activate the venv:

``` sh
.venv\Scripts\activate    # Windows
source .venv/bin/activate # MacOS and Linux
```

3. Install the project:

``` sh
pip install pyllo_greeting
```

4. Use the CLI:

``` sh
pyllo
# Output: Hello there
```

### Options

#### Name and Tones

- It is possible to pass a name/word to be greeted by the app:

``` sh
pyllo John
# Hello there, John
```

``` sh
pyllo everyone
# Hello there, everyone
```

> This argument is a string, therefore, in presence of empty spaces, it has to be passed in quotes:

``` sh
pyllo "Sergio and Sara"
# Hello there, Sergio and Sara
```

- Secondly, there is also the possibity of informing a tone. The default tone is "normal":

1. `Normal/Default`:

``` sh
pyllo Alice
# Hello there, Alice
```

2. `Quick`:

``` sh
pyllo Theresa --quick
# Hi, Theresa

pyllo Matthew -q
# Hi, Matthew
```

3. `Fancy`:

``` sh
pyllo Leticia --fancy
# Greetings. It is truly a pleasure to acknowledge your existence, Leticia

pyllo Beatrice -f
# Greetings. It is truly a pleasure to acknowledge your existence, Beatrice
```

#### Random Greet

When using the program with the `--random | -r` flag, the CLI will display a random greeting phrase.  
This random phrase can be one of the standards (normal, quick and fancy) or a completely different one.

``` sh
pyllo Antony --random
# Output: System check complete. Welcome, Antony.

pyllo Mary --random
# Output: Greetings, Mary.

pyllo Mark --random
# Output: What's up, Mark?
```

#### Meta Options

There are currently two `meta` options:

1. `App Version (--version | -v)`:

``` sh
pyllo -v
# 1.1.2
```

2. `App's Credits (--credits | -c)`:

``` sh
pyllo -c
# Project created by:
#         João Antônio

# Author's GitHub:
#         https://github.com/joao-antonio-la

# Project's Repository:
#         https://github.com/joao-antonio-la/pyllo
```