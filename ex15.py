#Faça um algoritmo que receba um número e diga se este número está no
# intervalo entre 100 e 200;
n = int(input('Digite um valor: '))
if n >= 100 and n<= 200:
    print('O número {} está no intervalo entre 100 e 200'.format(n))
else:
    print('O número {} não está no intervalo entre 100 e 200'.format(n))
