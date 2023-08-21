import numpy as np

lista_altura = [1.76, 1.70, 1.71]

list_array = np.array(lista_altura)

print('Média = ', np.median(list_array))

soma = 0

for altura in lista_altura:
    soma += altura
print('Soma das alturas = ', soma/3)