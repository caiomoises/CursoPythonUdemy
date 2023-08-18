'''
Sets são eficientes para remover valores duplicados de iteráveis.
- Seus valores sertão sempre únicos;
- Não aceita valores mutáveis;
- Não aceitam valores mutáveis;
- Não tem índexes;
- Não garantem ordem;
- São iteráveis (for, in, not in)
'''

# lista1 = [1, 2, 3, 3, 3, 3, 3, 3, 1]
# s1 = set(lista1)
# lista2 = list(s1)
# print('lista = ', lista2)
# print('set = ', s1)

'''
Métodos úteis:
- add, update, clear, discard
'''
# s1 = set()
# s1.add('Caio') # adiciona um valor ao set
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4)) # Atualiza o set com novos dados
# s1.discard(1) # Elimina dados do set
# s1.discard('Olá mundo')
# print(s1)

'''
Operadores úteis:
- união | união (union) - Une
- intersecção & (intersection) - Itens presentes em ambos
- diferença - Itens presentes apenas no set da esquerda
- diferença simétrica ^- Itens que não estão em ambos
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # une os dois sets
s3 = s1 & s2 # mostra os item presentes nos dois sets
s3 = s1 - s2 # mostra apenas os itens que estao no set da esquerda
s3 = s1 ^ s2 # mostra os itens que não estao presentes nos sets

print(s3)