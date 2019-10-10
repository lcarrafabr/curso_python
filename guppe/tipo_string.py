"""
Tipo String

Em Python, String é tudo o que estiver entre:

- Aspas simpes;
- Aspas duplas;
- Aspas simples triplas
- Aspas duplas triplas

Exemplos:

- Aspas simples -> 'Luciano Carrafa'
- Aspas duplas -> "Luciano Carrafa"
- Aspas simples triplas '''Luciano Carrafa'''
"""

nome = 'Luciano Carrafa Benfica'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Luciano \nCarrafa Benfica'
print(nome)
print(type(nome))

nome = """Luciano
Carrafa
Benfica"""
print(nome)
print(type(nome))

nome = 'Luciano Carrafa Benfica'
print(nome.upper())

nome = 'LUCIANO CARRAFA BENFICA'
print(nome.lower())

nome = 'LUCIANO CARRAFA BENFICA'
print(nome.title())

nome = 'Luciano Carrafa Benfica'
print(nome.split())

print(nome[0:7])

