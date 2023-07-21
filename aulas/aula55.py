'''
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
'''
import decimal

numero_1 = decimal.Decimal('0.1') # Utilizado mais em numeros com pontos flutuantes muito longos
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 3)) # Arredonda o valor decimal e mostra apenas ele inteiro

