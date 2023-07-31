'''
- Dicionários em Python (tipo dict)
- Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
- Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imtáveis como: 
str, int, float, bool, tuple, etc.
- O valor pode ser de qualquer tipo, incluindo outro 
dicionário.
- Usamos as chaves - {} - ou a classe dict para criar
dicionários.
- Imutáveis: str, int, float, bool, tuple.
- Mutável: dict, list.

pessoa = {
    'nome': 'Caio Moisés',
    'sobrenome': 'Cavalcante'
    'idade': 18,
    'altura': 1.76,
    'endereços': [
        {'rua': 'Sete de novembro', 'número': 431},
        {'rua': 'Padre carlos', 'número': 786}
    ]
}
print(pessoa, type(pessoa))
'''

pessoa = {
    'nome': 'Caio Moisés',
    'sobrenome': 'Cavalcante',
    'idade': 18,
    'altura': 1.76,
    'endereços': [
        {'rua': 'Sete de novembro', 'número': 431},
        {'rua': 'Padre carlos', 'número': 786}
    ]
}
print(pessoa['nome'], type(pessoa))
print()

for chave in pessoa:
    print(chave,':', pessoa[chave])