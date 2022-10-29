from random import randint
print('Jogo dos passos')
print('=-'* 20)
print('Passo 1')
jogador = int(input('Escolha seu primeiro passo [1], [2] ou [3]: '))
computador = randint(1,3)
for c in range(2,6):
    if jogador != computador:
        print('Passo {}'.format(c))
        jogador = int(input('Escolha seu primeiro passo [1], [2] ou [3]: '))
        if c == 5:
            print('Você ganhou!')
if jogador == computador:
    print('Bomba!')
    print('Comece de novo!')







