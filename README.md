# Interpret de forth

Un interpret de forth per la practica de compiladors de l'assignatura de llenguatges de programacio de la FIB.
La gramatica es escrita amb ANTLR i l'interpret en python.
Inclou tembe un joc de testos doctest.

## Components principals

- forth.g4: Defineix la sintaxis.

- EvalVisitor(forth.py): Implementa la semantica del llenguatge i executa les instruccions utilitzant el visitor.

- stack.py: Implementa la pila i les seves operacions

- boolean.py: Gestiona les operacions booleanes.  

## Instalació

### Prerequisits

- Python 3.x

### Setup amb Virtual Environment

1. Crear un virtual enviorment:

    python3 -m venv .venv
    ```
    ``` bash

2. Activar virtual environment:

    ```bash
    source .venv/bin/activate
    ```

3. Instalar dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Generar el parser ANTLR:

    ```bash
    make all
    ```

## Utilització
Per utilitzar l'interpret cal tenir instalat python3 i antlr4, llavors executar en la terminal desde la carpeta base del projecte:

```bash
python3 -i forth.py
o
make run
```

Per fer els testos es pot fer :

```bash
make test
```
