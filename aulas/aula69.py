'''
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
'''

# def duplica(valor):
#     return valor*2

# def triplica(valor):
#     return valor*3

# def quadruplica(valor):
#     return valor*4

# num = int(input('Insira um valor inteiro: '))

# valor_duplica = duplica(num)
# valor_triplica = triplica(num)
# valor_quadruplica = quadruplica(num)

# print(f'O valor {num} duplicado é {valor_duplica}')
# print(f'O valor {num} triplicado é {valor_triplica}')
# print(f'O valor {num} quadruplicado é {valor_quadruplica}')

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

num = int(input('Insira um valor inteiro: '))

valor_duplica = criar_multiplicador(2)
valor_triplica = criar_multiplicador(3)
valor_quadruplica = criar_multiplicador(4)

print(f'O valor {num} duplicado é {valor_duplica(num)}')
print(f'O valor {num} triplicado é {valor_triplica(num)}')
print(f'O valor {num} quadruplicado é {valor_quadruplica(num)}')