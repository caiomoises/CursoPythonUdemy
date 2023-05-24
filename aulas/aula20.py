valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

if valor1 > valor2:
    print(f'O valor {valor1} é maior que {valor2}!')
elif valor2 > valor1:
    print(f'O valor {valor2} é maior que {valor1}!')
elif valor1 == valor2:
    print('os valores informados são iguais!')