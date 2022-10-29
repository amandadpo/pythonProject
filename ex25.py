#Faça um algoritmo que leia dois números e identifique se são iguais ou
# diferentes. Caso eles sejam iguais imprima uma mensagem dizendo que eles
# são iguais. Caso sejam diferentes, informe qual número é o maior, e uma
# mensagem que são diferentes;
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
if n1 == n2:
    print('Números iguais!')
elif n1 > n2:
    print('{} maior que {}'.format(n1,n2))
else:
    print('{} menor que {}'.format(n1,n2))
