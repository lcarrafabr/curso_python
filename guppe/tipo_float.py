"""
Tipo Float

Tipo real, decimal

Cassas decimais

OBS: o separador de casas decimais na programação é o (.) ponto e não a virgula
"""
# Errado do ponto de vista do Float mas gera uma tupla
valor = 1,44

print(valor)
print(type(valor))

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# podemos converter um float em int
"""
Ao converter valores float para inteiros perdemos precisão
"""

res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos
variavel = 5j

print(type(variavel))
