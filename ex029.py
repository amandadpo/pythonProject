#Escreva um programa que leia a velocidade de um carro. Se ele
# ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite
velocidade = float(input('Informe a velocidade: '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade e foi multado em R$ {:.2f}'.format((velocidade - 80)*7))
else:
    print('Dirija com segurança!')
