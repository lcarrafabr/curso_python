"""
Listas

Lsitas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem
Dinâmico e também podermos colocar QUALQUER tipo de dado

Linguagens C/Java; Arrays
    - Possuiem tamanho e tipo de dado fixo:
    Ou seja, nestas lingugens, se você criar um array de tipo int e com tamanho 5, este array será SEMPRE do
    tipo int e poderá ter SEMPRE o máximo de 5 valores.

Já em Python:

 - Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e ir adicionando elementos.
 - Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja podemos colocar qualquer tipo de dado.

 As listas em Python são representadas por colchetes: []
"""

lista01 = [10,3,6,2,5,1,8,9,4,7,1,1,1,1]

lista02 = ['L','U','C','I', 'A', 'N', 'O', ' ', 'C', 'A', 'R', 'A', 'F', 'A']

lista03 = []

lista04 = list(range(11))

lista05 = list('Luciano Carrafa benfica')

#  Podemos facilmente cjhegar se determinado valor está contido na lista
num = 8
if num in lista04:
    print(f'Encontrei o numero: {num}')
else:
    print(f'Não encontrei o numero: {num}')


#  Podemos facilmente ordenar a lista
lista01.sort()
print(lista01)

#  Podeos facilmente contr o numero de ocorrências de um valor e muma lista
print(lista01.count(1))
print(lista05.count('n'))

#  Adicionar elementos em listas
"""
Para adicionar elementos em listas utilizamos a função append
"""
