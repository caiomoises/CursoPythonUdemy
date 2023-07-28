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
os.system('cls')

palavra_secreta = input('Digite uma palavra secreta: ')
dica = input('Insira uma dica para o jogador: ')
os.system('cls')
nome = input('insira seu nome: ')
os.system('cls')
letras_certas = ''
numero_tentativas = 0
chances = 15
print(f'Bom jogo, {nome}')
print('Dica:',dica)

while True:
    print(f'Tentativas restantes {chances}')
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    chances -= 1
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
        os.system('cls')
        print(f'Você acertou e concluiu a palavra, PARABÉNS {nome}!')
        print(f'A palavra formada é: {palavra_formada}')
        print(f'Número de tentativas: {numero_tentativas}')
        jogar_novamente = input('Deseja jogar novamente? ')

        if jogar_novamente.upper() == 'SIM':
            os.system('cls')
            palavra_secreta = input('Digite uma palavra secreta: ')
            dica = input('Insira uma dica para o jogador: ')
            os.system('cls')
            nome = input('insira seu nome: ')
            os.system('cls')
            letras_certas = ''
            numero_tentativas = 0
            chances = 15
            print(f'Bom jogo, {nome}')
            print('Dica:',dica)
            continue
        else:
            os.system('cls')
            print('Obrigado por ter jogado!')
            break
    if numero_tentativas == 15:
        print('Você não tem mais tentativas!')
        print(f'Mais sorte na proxima {nome}')
        break