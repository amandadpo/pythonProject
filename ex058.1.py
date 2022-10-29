from random import randint
cont = 0
computador = randint(0,10)
acertou = False
print('Vamos jogar! Você deverá advinhar o número que eu pensar!')
while not acertou:
    jogador = int(input('Digite um número de 0 a 10: '))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
         print('Chute um número mais baixo')
        else:
         print('Chute um numero mais alto')
print('Você ganhou! Eu também escolhi o número {}!Foram necessárias {} chances para você acertar!'.format(computador,cont))
