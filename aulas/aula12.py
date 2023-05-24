# Exercício de programação - Cálculo do IMC (Índice de Massa Corpórea) + Ellipsis
# ... esses tres pontos é chamado de Ellipsis e pode ser inserido no codigo para nao provocar erro
import os
nome = input('Qual o seu nome: ')
altura = float(input('Qual a sua altura em m: '))
peso = float(input('Qual o seu peso em kg: '))

imc = peso / (altura ** 2)
os.system('clear')
print(f'\n\n{nome} tem {altura}m, pesa {peso}kg e seu IMC é {imc}')
print(...) #Ellipsis