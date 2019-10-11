"""
 - Precisamos conhecero loop for para usar os ranges.
 - precisamos conhecero range para trabalhar melhor com loops for.

 Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória, mas sim
 de maneira especificada.

 Formas gerais:

 #  Forma 01
 range(valor_de_parada)

 OBS: valor_de_parada não inclusive (inicio padrão 0 (zero) e passo de 1 em 1)
"""

#  Forma 01
for num in range(11):
    print(num)


#  Forma 02
"""
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário e passo de 1 em 1)
"""
for num in range(5, 11):
    print(num)

#  Exemplo forma 03
"""
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário e passo de 1 em 1 e pa)
"""
