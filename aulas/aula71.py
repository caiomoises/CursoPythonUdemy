'''
Manipulando chaves e vaores em dicionários
'''

pessoa = {

}
chave = 'nome'

pessoa[chave] = 'Caio Moises' #Criando uma chave
pessoa['sobrenome'] = 'Cavalcante'

print(pessoa[chave])

pessoa[chave] = 'Kézia' # Edita a chave

del pessoa['sobrenome'] # Deleta uma chave

print(pessoa)
print(pessoa['nome'])

print(pessoa.get('sobrenome')) # Retorna None caso a chave não exista

