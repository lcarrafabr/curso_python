"""
Escopo de variáveis

Dois casos de escopo:

1- Variáveis globais:
    - Variaveis globais são reconhecidas, ou seja seu escopo compreende, todo o programa.

2 - Variáveis locais:
    - Variaveis locais são reconhecidas apenasonde foram declaradas, ou seja, seu escopo
    está limirado ao bloco onde foi declarado.

Para declarar variáveis em Python fazemos:

nome_da-variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que
ao declararrmos uma variavel, nós não colocamos o tipo de dado dela.
Este tipo é indeferido ao atribuirmos o valor a mesma.

Exemplo em C:
int numero = 42;

Exdemplo em Java
int numero - 42;
"""

numero = 42
print(numero)
print(type(numero))

numero = 'Luciano Carrafa benfica'
print(numero)
print(type(numero))

nao_existo = 'oi'
print(nao_existo)

numero = 2

if numero > 10:
    novo = numero + 10
    print(novo)

#  print(novo)
