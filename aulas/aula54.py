'''
Faça uma lista de compras com listas. O usuário deve ter a 
possibbilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
'''
import os

lista_compras = []
while True:
    os.system('cls')
    print('1 - Inserir produto; \n2 - Apagar produto;\n3 - Listar produtos. \n4 - SAIR\n')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        os.system('cls')
        novo_produto = input('Insira o novo produto: ')
        lista_compras.append(novo_produto)
    elif op == 2:
        apaga_produto = input('Indice do produto que deseja apagar? ')

        try:
            os.system('cls')
            delete = int(apaga_produto)
            del lista_compras[delete]
            print('Produto apagado com sucesso! ')
        except:
            os.system('cls')
            print('Item não encontrado! ')
    elif op == 3:
        os.system('cls')
        if len(lista_compras) == 0:
            print('A lista esta vazia!')
        else:
            os.system('cls')
            for i, nome in enumerate(lista_compras):
                print(i, nome)
    elif op == 4:
        os.system('cls')
        print('Obrigado por usar este programa!')
        break
    else:
        print('Por favor, insira uma das opções validas: ')