'''
Retorno de valores das funções (return) 

args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args): 
    total = 0
    for numero in args:
        print(numero)
        total += numero
    return total
soma1 = soma(1, 2, 3, 4, 5, 6)
print(soma1)

numeros = 1, 2, 3, 4, 5, 6
print(sum(numeros))


# def soma(x, y):
#     return x + y

# soma1 = soma (1, 2)
# soma2 = soma(3, 3)

# print(f'Soma = {soma1 + soma2}')