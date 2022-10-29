#Faça um programa que leia uma frase pelo teclado e mostre quantas
# vezes aparece a letra “A”, em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A posição do primeiro "A": {}'.format(frase.find('A')+1))
print('A posição do último "A": {}'.format(frase.rfind('A')+1))