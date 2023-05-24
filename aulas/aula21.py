# Operador logico 'and'

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '12345678'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada == 'S':
    print('Sair')
else:
    print('Senha incorreta')


# Avaliação de curto circuito
print(True and False and True)
print(bool(' '))# 0 0.0 '' False - são avaliados como valores falsos

if 1 and 1:
    print(True and 1 and False)