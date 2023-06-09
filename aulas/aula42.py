# while - Qual letra apareceu mais vezes na frase? (Iterando strings com while)
import os
os.system('clear')

""" frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.' """

frase = 'aaaooooeeeeeiiiiiiuuuuuuu'

#print(frase.count('Python')) # Quantas vezes a palavra Python aparece na frase

i = 0
qtd_mais_vezes = 0
letra_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quant_letra = frase.count(letra_atual)

    if qtd_mais_vezes < quant_letra:
        qtd_mais_vezes = quant_letra
        letra_mais_vezes = letra_atual

    #print(i, letra_atual, quant_letra) 
    i += 1
print(f'A letra que apareceu mais vezes foi "{letra_mais_vezes}" '
      f'que apareceu {qtd_mais_vezes}x')