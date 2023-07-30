'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Bom dia')

for nome in ['Caio', 'Kézia', 'João']:
    print(falar_bomdia(nome))
    print(falar_boanoite(nome))