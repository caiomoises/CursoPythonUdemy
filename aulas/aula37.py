# while + continue - pulando alguma repetição
'''
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
'''

import os
os.system('clear')

contador = 0

while contador < 100:
    contador += 1

    if contador == 6:
        print('Não tem o 6')
        continue
    if contador >= 10 and contador <= 27:
        print('Os números de 10 a 27 não serão exibidos')
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')