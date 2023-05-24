# id - A identidade do valor que está na memória
# Flags, is, is not e None
""" 
Flag (Bandeira) - Marcar um local
None - Não valor 
is e is not - é ou não é (tipo, valor, identidade)
id = identidade 
"""

condicao = False
passou_no_if = None #None

if condicao:
    passou_no_if = True #flag
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None) #is
print(passou_no_if, passou_no_if is not None) #is not

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))