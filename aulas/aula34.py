# while e break - Estrutura de repetição (Parte 1)
'''
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
'''

import os
os.system('clear')

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')

    if nome  == 'sair':
        break

    print(f'Seu nome é {nome}')

print('Saiu.')

