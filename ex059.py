#Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
opção = 0
while opção != 5:
    print('''Opções:  
     [ 1 ] somar
     [ 2 ] multiplicar
     [ 3 ] maior
     [ 4 ] novos números
     [ 5 ] sair do programa''')
    print('='*27)
    opção = int(input('>>>>>> Digite sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1,n2,soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('{} x {} = {}'.format(n1,n2,multiplicação))
    elif opção == 3:
        if n1 > n2:
            print('{} maior que {}'.format(n1,n2))
        else:
            print('{} maior que {}'.format(n2,n1))
    elif opção == 4:
        n1 = float(input('Digite o 1º número: '))
        n2 = float(input('Digite o 2º número: '))
    elif opção == 5:
        print('Finalizando o programa...')
    else:
        print('Digite uma opção válida!')
        print('-'*20)
print('FIM')

