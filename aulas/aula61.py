'''
CPF: 746.824.890-70
Colete a soma dos 9 promeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10


Ex.: 746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 =  7
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta

O primeiro digito do CPF é 7
'''

import sys
import random

cpf = ''
for index in range(9):
    cpf += str(random.randint(0,9))
# print(*cpf[:9])

index = 10
soma = 0

for num in cpf[:9]:
    multipl = int(num) * index
    # print(multipl, end=' ')
    index -= 1
    soma = soma + multipl 
 
# print(f'\nA soma dos valores acima é: {soma}')
multi_10 = soma * 10 
# print(f'Multiplicando {soma} por 10, temos: {multi_10}')
resto_divisao = multi_10 % 11
if resto_divisao > 9:
    resto_divisao = 0    
    # print(resto_divisao)
#     print('\nO 10º digito do seu CPF é: 0')
    # print(resto_divisao)
else:
    resto_divisao = resto_divisao
#     print(f'\nO 10º digito do seu CPF é: {resto_divisao}')

# valido = input('\nO digito acima é o 10º valor do seu CPF? ')
valido = True
if valido == True:
    novo_cpf = cpf + str(resto_divisao)
    # print('\n',*novo_cpf[:10])
    index = 11
    soma = 0

    for num in novo_cpf[:10]:
        multipl = int(num) * index
        # print(multipl, end=' ')
        index -= 1
        soma = soma + multipl 

    
    
    multi_10 = soma * 10 
    resto_divisao = multi_10 % 11
    if resto_divisao > 9:
        resto_divisao = 0
        # print(resto_divisao)
        # print('\nO 11º digito do seu CPF é: 0')
    else:
        resto_divisao = resto_divisao
        # print(resto_divisao)
        
else:
    sys.exit()

cpf_gerado = f'{novo_cpf[:10]}{resto_divisao}'
print(cpf_gerado)
print(f'CPF gerado: {cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:11]}')
# if cpf_gerado == cpf:
#     print(f'O CPF {cpf_gerado} é valido!')
# else:
#     print('O CPF informado é invalido !')