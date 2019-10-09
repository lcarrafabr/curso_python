"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, String é tudo o que estiver entre:

- Aspas simpes;
- Aspas duplas;
- Aspas simples triplas
- Aspas duplas triplas

Exemplos:

- Aspas simples -> 'Luciano Carrafa'
- Aspas duplas -> "Luciano Carrafa"
- Aspas simples triplas '''Luciano Carrafa'''

Todo este comentário está em aspas duplas triplas

"""
# Entrada de dados
# print('Qual o seu nome? ')
# nome = input() # Imput -> Entrada

nome = input('Qual o seu nome? ')

# Exemplo de print antigo da versão 2x
# print('Seja bem-vindo(a) %s' % nome.title())

# Exemplo de print 'moderno' 3.x
# print('Seja bem vindo(a) {0} ' .format(nome))

# Exemplo de print atual 3.7
print(f'Seja bem vindo(a) {nome.title()}')

# print('Qual a sua idade? ')
# idade = input()

idade = int(input('Qual a sua idade? '))

# Processamento

# Saída

# print('O user %s tem %s anos' % (nome.title(), idade))

# Exemplo de print 'moderno' 3.x
# print('user {0} tem {1} ' .format(nome.title(), idade))


print(f'User {nome.title()} tem {idade} anos')

# print(f'O usuário(a) {nome.title()} nasceu em {2018 - int(idade)}') # int(idade) => cast

print(f'O usuário(a) {nome.title()} nasceu em {2018 - idade}')  # int(idade) => cast
