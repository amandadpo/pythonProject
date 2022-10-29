from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('Vamos jogar jokenpô?')
print('''Escolha
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('='*30)
print('Jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('='*30)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Opção inválida!')
elif computador == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador venceu!')
    elif jogador == 0:
        print ('Computador venceu!')
    else:
        print('Opção inválida!')
elif computador == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    else:
        print('Opção inválida!')




