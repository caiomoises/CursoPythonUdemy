''' Interpolação de string com % em Python
s - string
d ou i - int
f - float
x - X - hexadecimal (ABCDEF0123456789)
'''
nome = 'Caio Moisés'
preco = 1234.45678
variavel = '%s, o preço é %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %X' % (15235, 15235))