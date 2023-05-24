# Uma introdução às f-strings (formatação de strings)
nome = input('Qual o seu nome: ')
altura = float(input('Qual a sua altura em m: '))
peso = float(input('Qual o seu peso em kg: '))

imc = peso / (altura ** 2)

print(f'\n\n{nome} tem {altura:.2f}m, pesa {peso:.2f}kg e seu IMC é {imc:.2f}')