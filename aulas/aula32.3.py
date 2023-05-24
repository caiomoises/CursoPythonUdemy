# Exercícios
'''
Faça um programa que peça o primeiro nome do usuario, se o nome tiver: 
4 letras ou menos esceva: "Seu nome é curto";
entre 5 e 6 letras: "Seu nome é normal";
se tiver mais de 6: "Seu nome é muito grande".
'''

nome = input('Digite seu primeiro nome: ')

tam_nome = len(nome)

if tam_nome > 1:
    if tam_nome <= 4:
        print('Seu nome é pequeno')
    elif tam_nome > 4 and tam_nome <= 6:
        print("Seu nome é normal")
    else:
        print('Seu nome é muito grande!')
else:
    print('Digite mais letras')