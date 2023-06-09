# Introdução ao for / in - estrutura de repetição para coisas finitas
import os
os.system('clear')

texto = 'Python'
novo_texto = ''
for i in texto:
    novo_texto += f'*{i}'
    print(i)
    
novo_texto += '*'
print(novo_texto)