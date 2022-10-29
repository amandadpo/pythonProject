#Escreva um algoritmo que leia dois valores inteiros distintos e
# informe qual é o maior;
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1,n2))
else:
    print('{} é maior que {}'.format(n2,n1))
