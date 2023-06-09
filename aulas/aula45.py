# Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)
'''
Iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entrega o proximo valor
iter -> me entrega seu iterador
'''
import os
os.system('clear')

texto = iter('Moisés') # .__iter__()

print(texto.__next__())
print(next(texto)) #.__next__())
print(next(texto)) #.__next__())
print(next(texto)) #.__next__())
print(next(texto)) #.__next__())
print(next(texto)) #.__next__())


texto1 = 'Caio Moisés' #Iteravel
iterador = iter(texto1) #Iterador

for letra in texto1:
    print('*', letra)