#Faça um algoritmo que receba “N” números e mostre positivo, negativo
# ou zero para cada número;
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número: '))
    if n > 0:
        print('{} é POSITIVO!'.format(n))
    elif n == 0:
        print('0')
    else:
        print('{} é NEGATIVO!'.format(n))
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()
print('FIM')
