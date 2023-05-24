''' Peça ao usuario para digitar seu nome e idade
    Exiba: seu nome 
    o nome invertido 
    se o nome contem ou não espaços,
    quantidade de letras
    a primeira letra do nome
    a ultima letra do nome

    Se nada for digitado em nome ou idade: 
        exiba: 'Desculpe, vocẽ deixou campos vazios'. '''
import os

nome = input('Digite seu nome: ')
idade = input('Sua idade? ')
os.system('clear')
if nome and idade:
    print(20 * '-')
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços!')
        print(f'Seu nome tem {len(nome)-1} letras ')
    else:
        print('Seu nome não contém espaços!')
        print(f'Seu nome tem {len(nome)} letras ')
        
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
    print(20 * '-')
else:
    print('Desculpe, vocẽ deixou campos vazios')