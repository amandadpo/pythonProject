#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um
# número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
cont = 0
jogador = 0
computador = randint(0,10)
while jogador != computador:
    jogador = int(input('Escolha um número entre 0 e 10: '))
    cont += 1
    if jogador != computador:
        print('Você errou, tente de novo')
    else:
        print('Parabéns, vc acertou! Você escolheu {} e eu também escolhi {}!'.format(jogador,computador))
        print('Você precisou de {} chances para acertar'.format(cont))
print('FIM')


