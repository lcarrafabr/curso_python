"""
Estruturas lógicas:

and (e), or (ou), not (não), is (é)

Operadores unários:
     - not

Operadores binários:
    - and, or, is

regras de funcionamento

Para o and, amobos os valores precisam ser True
Para o or, um ou outro valor precisam ser true
Para o not o valor do booleano é invertido (se for true vira false e se for false vira true)
"""

ativo = False
logado = True

if ativo and logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta, por favor realize os procedimentos %$#%¨$$##')

if not ativo:
    print('Você precisa ativar sua conta, por favor não use licença pirata')

print(not False)

if logado is False:
    print('Realize o login no sistema')

