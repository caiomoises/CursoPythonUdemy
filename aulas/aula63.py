'''
Argumentos nomeados e nao nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)


Valores padrão para parâmetros 
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja 
enviado para o prâmetro, o valor padrão será usado.
Refatorar: editar o seu código.
'''

# def soma(x, y, z):
      # Definição
#     print(f'{x=}, {y=}, {z=}', '|', 'X + y + z = ', x + y + z)

# soma(1, 2, 3)
# soma(x=1, y=2, z=3)


def sum(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x+y+z)
    else:
        print(f'{x=} {y=}', x+y)

sum(1, 2)
sum(3, 5)
sum(100, 200)
sum(7, 9, 0)