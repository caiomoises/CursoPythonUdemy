# Operadores in e not in
#Strings em python são iteráveis
# 0 1 2 3 4 5
# M o i S É S
#-6-5-4-3-2-1

"""nome = 'Moisés'
print(nome[4])
print(nome[-2]) 
print('é' in nome)
print('z' in nome)
print('sés' in nome)
print(10*'-')
print('é' not in nome)
print('z' not in nome)
print('sés' not in nome) """

nome = input('Insira um nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')