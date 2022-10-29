#Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem
# informando “maior de idade” e “menor de idade” para cada pessoa.
# Considere a idade a partir de 18 anos como maior de idade;
for c in range(1,6):
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        print('Maior de idade')
        print('=' * 20)
    else:
        print('Menor de idade')
        print('=' * 20)
