''' While/else -> o else é executado junto com o while,
a menos que haja um break dentro do while''' 
import os
os.system('clear')

string = 'Valor qualquer'

i = 0
print('Você está no WHILE')
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('Você esta no ELSE:\n', string)