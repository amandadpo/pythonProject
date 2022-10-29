#Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triangulo
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')



