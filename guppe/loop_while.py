"""
Loop While

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.
"""

#  Exemplo 01
numero = 1

while numero <= 10:
    print(numero)
    numero = numero + 1


#  Exemplo 02
resposta = ''

while resposta != 'sim' and resposta != 's':
    resposta = input('Já acabou?\n')


