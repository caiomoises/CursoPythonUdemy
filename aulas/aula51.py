'''
Introdução a desempacotamento.
'''

nomes = ['Caio', 'Kézia', 'Marcelo', 'Rivania']
nome1, nome2, nome3, nome4 = nomes

print(nome2)

nome1, *_ = ['Caio', 'Kézia', 'Marcelo', 'Rivania']

print(nome1)