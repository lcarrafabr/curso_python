"""
PEP 8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

Zen of Python

import this

A idéia da pep8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

class Claculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes emminusculo separados por underline para funções ou variavéis.

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação! (Não use tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições declasse com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports

-Inports devem ser sempre feitos em linhas separadas;

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problremas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote recomenda-se fazer:

from types import{
    StringType,
    ListType,
    SetType,
    OutroType
}

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de contantes
e comentários globais.

[6] - Espaços em expressões e instrunções

# Não faça:

funcao( algo[1], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não fala:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

#Faça:

dict['chave'] = lista[indice]

# Não faça:

x     = 1
y     = 2

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - termine sempre uma instrunção com uma nova linha

"""
import this
