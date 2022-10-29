#Radar
velocidadeVeiculo = float(input('Digite a velocidade do veículo: '))
if velocidadeVeiculo <= 50*1.1:
    print('Isento')
elif velocidadeVeiculo <= 70:
    print('Multado com 3 pontos na carteira!')
elif velocidadeVeiculo <=90:
    print('Multado com 5 pontos na carteira!')
else:
    print('Multado com 7 pontos na carteira!')
