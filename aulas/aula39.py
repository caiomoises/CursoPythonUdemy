# Exercício guiado com while
'''
Iterando strings com while
'''
import os
os.system('clear')


#       012345678910
nome = 'Caio Moisés' #Iteráveis

""" 
print(nome)
print(tamanho_nome)
print(nome[3])  """

tamanho_nome = len(nome)
indece = 0
novo_nome = ''
while indece < tamanho_nome:
    letra = f'*{nome[indece]}'
    novo_nome += letra
    indece += 1

novo_nome += '*'
print(novo_nome) 