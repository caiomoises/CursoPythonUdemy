# Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string
'''
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis que vimos: str, int, float, bool
'''
import os
os.system('clear')

string = 'caiO moiSés'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'I' #Não consegue mudar porque é imutavel
print(string.capitalize().title())
print(outra_variavel.capitalize().title())