''' Operador logico 'or' se qualquer valor for considerado verdadeiro
a expressão inteira será validada naquele valor.
''' 
entrada = input('[E]ntrar [S]air: ')
entrada_maiuscula = entrada.capitalize()
senha_digitada = input('Senha: ') or 'Sem senha'

senha_permitida = '12345678'
if entrada_maiuscula == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada == 'S':
    print('Sair')
elif senha_digitada == 'Sem senha':
    print(senha_digitada)
else:
    print('Opção de entrada ou senha incorreta')