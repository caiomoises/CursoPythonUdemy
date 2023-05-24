#  Introdução aos blocos de código + if / elif / else (condicionais)
entrada = input('Você quer "entrar" ou sair? ')

if entrada == 'entrar':
    print('Seja bem vindo!')
elif entrada == 'sair':
    print('Até mais!')
else: 
    print('Opção inválida')