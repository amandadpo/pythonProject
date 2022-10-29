#Faça um algoritmo que receba um número e mostre uma mensagem caso este
# número seja maior que 80, menor que 25 ou igual a 40;
n = int(input('Digite um número: '))
if n > 80:
    print('Número maior que 80!')
elif n < 25:
    print('Número menor que 25!')
elif n == 40:
    print('Número igual a 40!')