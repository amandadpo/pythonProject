#Escreva um programa que faça o computador “pensar” em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador.O programa deverá escrever na tela se
# o usuário venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0,5)
print('Vamos jogar!Você deve advinhar o número que eu vou pensar!')
print('Escolha um número entre 0 e 5')
print('-=-'*20)
jogador = int(input('Digite o número: '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print('Você errou!Eu pensei no número {}'.format(computador))










