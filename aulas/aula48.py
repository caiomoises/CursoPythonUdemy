# Tipo list - Introdução às listas mutáveis em Python
'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - Índices e fatiamento
Metodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indece escolhido
    del - Apaga um indice
    clear - Limpa a lista
    extend - estende a lista
    + - Concatena listas
Create Read Update   Delete (CRUD)
Criar, ler, alterar, apagar = lista[i] 
'''

#......+01234
#......-54321

string = 'ABCDE' # 5 caracteres (len)

list = [123, True, 'Caio Moisés', 1.2] # Suporta vários valores de qualquer tipo
list[2] = 'José Mateus' # Mudando o valor que esta no indice 2 da lista
print(list)
del list[3] # Apaga o indice 3 da lista
print(list)
list.append(50) # Adiciona um valor ao final da lista
print(list)
removido = list.pop()  # Remove o ultimo iten da lista, nesse caso o 50
list.append(60)
print(list, 'Removido, ', removido)

list.insert(0, 5) #primeiro valor é um indice no qual desejo inserir algo, o segundo é o que será add
print(list)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # Concatenando duas listas
lista_a.extend(lista_b) # Fazendo a lista b virar uma extensão da lista a 
print(lista_c)
print(lista_a)