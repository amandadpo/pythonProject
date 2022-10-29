aluguel = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados?: '))
dia = (60 * aluguel) + (0.15 * km)
print('O valor a pagar pelo aluguel do carro é: {}'.format(dia))
