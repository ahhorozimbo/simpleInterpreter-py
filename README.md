# Simple Interpreter (Python)

Interpretador escrito em Python para uma linguagem mínima de expressões matemáticas, com **variáveis** (prefixo `$`), **atribuição**, **parênteses**, as quatro operações e **`print`**. Trabalho de Compiladores.

O interpretador tem um **analisador léxico** (`SimpleLexer.py`), que transforma o texto em tokens (`tokens.py`), e um **analisador sintático descendente recursivo** (`SimpleParser.py`), que avalia as expressões enquanto lê.

## Exemplo

`text.txt`:

```
$x = 2 - 2 + 2/5;
$y = 2 * 10 + 1;
$z = ($x + $y) * 5;
$p = 3.14;
print($z);
```

```bash
cd simple-interpreter-master
python __main__.py
```

Saída: `103.0`.

## Limitação conhecida

A subtração e a divisão são avaliadas da direita para a esquerda: `2 - 2 + 2/5` vira `2 - (2 + 0.4) = -0.4`, e não `0.4`. Por isso o exemplo imprime `103.0` em vez de `107.0`. A correção é fazer o parser acumular os termos num laço (associatividade à esquerda) em vez de usar recursão à direita.

## Créditos

Baseado em [wellingtondellamura/compiler-from-scratch](https://github.com/wellingtondellamura/compiler-from-scratch) e [davidcallanan/py-simple-math-interpreter](https://github.com/davidcallanan/py-simple-math-interpreter).
