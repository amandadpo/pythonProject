real = float(input('Informe quantos reais você possui: R$ '))
dolar = real / 5.18
euro = real / 5.19
print('Com a quantia que você possui, é possível comprar U${:.2f} \n e {:.2f} euros.'.format(dolar,euro))
