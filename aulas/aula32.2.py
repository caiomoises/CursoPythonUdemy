# Exercícios
'''
Faça im programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. 
Ex: Bom dia 0-12, Boa tarde 12-18, Boa noite 18-00
'''

hora = input('Digite as horas: ')

if hora.isdigit():
    hora_int = int(hora)
    if hora_int >= 0 and hora_int < 12:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int < 18:
        print('Boa tarde!')
    else:
        print('Boa noite!')
else:
    print('Você nao digitou as horas!')