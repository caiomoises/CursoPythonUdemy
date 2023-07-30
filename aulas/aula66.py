'''
Exercicios com funções

crie uma função que multiplique todos os argumentos 
nao nomeados recebidos
Retorne o total para uma variavel e mostre o valor 
da variável.

Crie uma função que fala se um numero é par ou ímpar.
Retorne se o número é par ou ímpar.
'''

def multiplique(*args):
    total = 1
    for valor in args:
        total *= valor
    return total

def par_impar(val):
        # val = int(val)
        if val % 2 == 0:
            return ('o valor informado é par')
        return ('O valor informado é Ímpar')
    
valores = (1, 2, 3, 4)

mult = multiplique(*valores)
print(f'A multiplicação dos valores é: {mult}')

valor = int(input('Insira um valor inteiro: '))

impa_par = par_impar(valor)
print(impa_par)