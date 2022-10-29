#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento
print('{:=^40}'.format(' Lojas Amandita '))
preço = float(input('Valor das compras: '))
pagamento = int(input(''' FORMAS DE PAGAMENTO
[1] À vista
[2] Cartão direto
[3] 2x no cartão
[4] Parcelado em 3x ou mais
Digite o número que corresponde a forma de pagamento: '''))
if pagamento == 1:
    print('Você terá 10% de desconto.\n'
          'O valor a pagar é R$ {}'.format(preço-preço*0.1))
elif pagamento == 2:
    print('Você terá 5% de desconto. \n'
          'O valor a pagar é R$ {}.'.format(preço-preço*0.05))
elif pagamento == 3:
    print('O valor a pagar é R$ {}. \n'
          'O valor de cada parcela será de R$ {}'.format(preço,preço/2))
elif pagamento == 4:
    p1 = int(input('Quantas vezes irá parcelar? '))
    parcela = preço+preço*0.2
    print('Você pagará 20% de juros.\n'
          'O valor total a pagar é R$ {} em {}x.\n'
          'O valor de cada parcela será de R$ {}'.format(parcela,p1,parcela/p1))
else:
    print('Dígito inválido!')



