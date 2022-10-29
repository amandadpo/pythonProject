#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
# 200Km e R$0,45 parta viagens mais longas.
distância = float(input('Digite a distância percorrida: '))
if distância <=200:
    print('Você pagará R${} pela passagem'.format(distância*0.5))
else:
    print('Você pagará R${} pela passagem.'.format(distância*0.45))