"""
Saindo de loops com breaks

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.
"""

#  Exemplo 01
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saí do loop')

#  Exemplo 02
while True:
    comando = input('Digite "s" para patrar o programa.\n')
    if comando == 's':
        break


