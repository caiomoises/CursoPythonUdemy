# range + for para usar intervalos de números
'''
for + range

range -> range(start, stop, step)
'''
import os
os.system('clear')

#numero = range(10) # de 0 a 10
#numero = range(5, 10) # de 5 a 10
#numero = range(5, 10, 2) # de 5 a 10 pulando de 2 em 2
#numero = range(0, -10, -1) # de 0 a -10 decrementando -1
numero = range(0, 100, 2) # Números pares de 0 a 100

#print(numero)

for i in numero:
    print(i)