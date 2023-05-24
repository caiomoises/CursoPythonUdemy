# Parte 1: Variáveis, constantes e complexidade de código
'''
CONSTANTE = 'variaveis' que não vão mudar 
Muitas condições no mesmo if -> ruim <- contagem de complexidade ruim
'''

velocidade = 61 # Velocidade atual do carro
local_do_carro = 101 # Local em que o carro esta na estrada

RADAR_1 = 60 # Velocidade maxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_do_carro >= (LOCAL_1 - RADAR_RANGE) and local_do_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

# Deixando o codigo mais legivel
if velocidade_carro_passou_radar_1:  
    print('Velocidade do carro passou do permitido no RADAR 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print('Carro multado no radar 1 ')