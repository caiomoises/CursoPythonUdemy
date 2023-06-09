'''
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar uma letra por vez.
- Quando o usuário digitar uma letra, você vai conferir se a letra
digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
'''
import os
os.system('clear')

palavra_secreta = input('Digite uma palavra secreta: ')
dica = input('Insira uma dica para o jogador: ')
os.system('clear')
letras_certas = ''
numero_tentativas = 0
print('Dica:',dica)

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:',palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Você acertou e concluiu a palavra, PARABÉNS!')
        print('A palavra formada é:',palavra_formada)
        print('Número de tentativas:', numero_tentativas)
        jogar_novamente = input('Deseja jogar novamente? ')

        if jogar_novamente.upper() == 'SIM':
            os.system('clear')
            palavra_secreta = input('Digite uma palavra secreta: ')
            dica = input('Insira uma dica para o jogador: ')
            os.system('clear')
            letras_certas = ''
            numero_tentativas = 0
            print('Dica:',dica)
            continue
        else:
            os.system('clear')
            print('Obrigado por ter jogado!')
            break