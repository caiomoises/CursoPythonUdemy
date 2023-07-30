'''
Higher Order Functions - funções que podem receber e/ou retornar outras funções
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc)


Funções de primeira classe
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, texto, nome):
    return funcao(texto, nome)

v = executa(saudacao, 'Bom dia', 'Caio')
f = executa(saudacao, 'Bom dia', 'Kézia')
print(v)
print(f)
