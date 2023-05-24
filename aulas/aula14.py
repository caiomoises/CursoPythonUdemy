# Formatação de strings com o método format
nome = input('Qual o seu nome: ')
altura = float(input('Qual a sua altura em m: '))
peso = float(input('Qual o seu peso em kg: '))

imc = peso / (altura ** 2)

print('\n\n{} tem {:.2f}m, pesa {:.2f}kg e seu IMC é {:.2f}'.format(nome, altura, peso, imc))