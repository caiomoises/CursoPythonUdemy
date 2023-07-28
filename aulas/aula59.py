'''
Desenpacotamento em chamadas de métodos e funções
'''
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'Legal'

# a, b, *_ ,c = lista # *_ representa o resto da lista
# print(a, c)

for nome in lista:
    print(nome, end=' ') # Desempacotamento

print(*lista)
print(*string)
print(*tupla)


salas = [
    ['Maria', 'Helena', 'João', 'Pedro'],
    ['Elaine'],
    ['Luiz', 'Lucas', 'Eduarda']
]

print(*salas, sep='\n')