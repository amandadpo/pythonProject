#Faça um algoritmo que receba um número e mostre uma mensagem caso
# este número seja maior que 10;
n = int(input('Digite um número: '))
if n > 10:
    print('O número {} é maior do que 10'.format(n))
elif n < 10:
    print('O número {} é menor do que 10'.format(n))
else:
    print('10 é igual a 10')
