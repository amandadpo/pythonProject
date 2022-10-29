#A Loja Mamão com Açúcar está vendendo seus produtos em 5(cinco)prestações
# sem juros. Faça um algoritmo que receba um valor de uma compra e mostre
# o valor das prestações;
produto = float(input('Digite o valor do produto R$ '))
parcelas = produto/5
print('O valor de cada prestação será de R$ {:.2f}'.format(parcelas))
