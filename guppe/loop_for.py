"""
loop For

Loop -> Estrutura de repetição.

For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //Execuçãodo loop
}

#  Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis:

- String
    nome = 'Luciano'

- Lista
    lista = [1, 2, 3, 4, 5]

- Range
    numeros = range(1, 10)
"""

nome = 'Luciano Carrafa Benfica'
lista = [1, 2, 3, 4,5,6,7,8,9, 10]
numeros = range(1, 10)  #  Este ainda tem que transformar em uma lista

#  Exemplo de for 01 (Iterando sobre uma String)
for letra in nome:
    print(letra, end='')

#  Exemplo de for 02 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

#  Exemplo de for 03 (Iterando sobre um range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive. no exemplo abaixo imprime de 1 a 9

1 - sim
2 - sim
3 - sim
4 - sim
5 - sim
6 - sim
7 - sim
8 - sim
9 - sim
10 - não
"""
for numero in range(1, 10):
    print(numero)

for i, v in enumerate(nome):
    print(i)

qtd = int(input('Quantas veses esse for deve rodar?\n'))

for n in range(1, qtd + 1):
    print(f'Imprimindo {n}')


"""
Printando emoji no terminal
"""
#  Original: U+1F601
#  Modificado U0001F601

#  https://apps.timwhitlock.info/emoji/tables/unicode

for num in range(1, 11):
    print('\U0001F601' * num)
