#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
n = int(input('Digite um nº: '))
u = n // 1 % 10
d = (n // 10 % 10) * 10
c = (n // 100 % 10) * 100
m = (n // 1000 % 10) * 1000
print('A unidade é: {}'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('O milhar é: {}'.format(m))