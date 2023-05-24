# Exercícios
'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():
    entrada_int = int(numero_inteiro)

    if entrada_int % 2 == 0:
        print('O número informado é par!')
    else:
        print('O número informado é impar')
else: 
    print('Você não digitou um número inteiro')