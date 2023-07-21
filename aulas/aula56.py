'''
split e join com lista e str
split - divide uma string
join - une uma string
'''

frase = '    olha só que,    coisa interessante'
lista_de_palavras = frase.split(',') #dividi toda as palavras da string

lista_frases = []
for i, frase in enumerate(lista_de_palavras):
    lista_frases.append(lista_de_palavras[i].strip())

# print(lista_de_palavras)
# print(lista_frases)

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)