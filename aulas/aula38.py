# while + while (laços internos)
'''
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
'''

import os
os.system('clear')

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    print('')

    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('\n Acabou')