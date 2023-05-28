# Exercício guiado - Calculadora - Parte 1
'''
Calculadora com While
'''
import os
os.system('clear')

condicao = True

while condicao:
    n1 = int(input('insira um valor inteiro: '))
    n2 = int(input('insira outro valor inteiro: '))
    op = input('Qual tipo de operadoração deseja fazer "+ - * /": ')
    print('\nResponda sim ou nao!')
    saida = input(f'Deseja realizar a operação {n1}{op}{n2}? ')
    saida = saida.capitalize()

    if saida == 'Sim':
        if op == '+':
            print('O resultado da operação é',n1+n2)
            print('')
        elif op == '-':
            print('O resultado da operação é',n1-n2)
            print('')
        elif op == '*':
            print('O resultado da operação é',n1*n2)
            print('')
        elif op == '/':
            print('O resultado da operação é',n1/n2)
            print('')
    else:
        os.system('clear')
        print('\nObrigado por usar esta calculadora')
        break
    