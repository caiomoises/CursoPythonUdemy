'''
Métodos úteis dos dicionarios em Python
len - quantas chaves 
keys - iteráveis com as chaves
values - iteráveis com chaves e valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item adicionado
pop - Apaga um item com a chave especificada (del)
update - atualiza um dicionario com outro
'''

# pessoa = {
#     'nome': 'Caio Moisés',
#     'sobrenome': 'Cavalcante'
# }

# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())

# pessoa.setdefault('idade', 40)
# print(pessoa['idade'])



# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }

# d2 = d1.copy()

# d2['c1'] = 1000
# d2['l1'][1] = 9999 

# print(d1)
# print(d2)

pessoa = {
    'nome': 'Caio Moisés',
    'sobrenome': 'Cavalcante'
}

# print(pessoa.get('nome', 'não existe'))

# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)

pessoa.update({
    'nome': 'novo',
    'idade': 18
})

print(pessoa)