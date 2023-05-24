# Introdução ao try e except para capturar erros (exceptions)
# try -> tentar executar o codigo
# except -> ocorreu algum erro ao tentar executar

""" print(1234)
print(4568)
int('a') """ # ValueError: invalid literal for int() with base 10: 'a'

numero_str = input('Vou dorar o número que você digitar: ')

try:
    print('STR:', numero_str)
    numero_f = float(numero_str) # Captura o erro na seção
    print('FLOAT:', numero_f)
    print(f'O dobro de {numero_str} é {numero_f * 2}')
except:
    print('Isso não é um número')


"""
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2}')
else:
    print('Isso não é um número!') """

