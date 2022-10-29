#Faça um algoritmo que leia um número de 1 a 5 e escreva por extenso.
# Caso o usuário digite um número que não esteja neste intervalo, exibir a
# seguinte mensagem: número inválido;
n = 0
while n <= 5:
    n = int(input('Digite um número de 1 a 5 ou [6] para sair do programa: '))
    if n == 1:
        print('1 - um')
    elif n == 2:
        print('2 - Dois')
    elif n == 3:
        print('3 - Três')
    elif n == 4:
        print('4 - Quatro')
    elif n == 5:
        print('5 - Cinco')
    elif n == 6:
        print('Finalizando... \n FIM')
    else:
        print("Digite uma opção válida!")

