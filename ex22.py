#Faça um algoritmo que receba o preço de custo e o preço de venda de 40
# produtos. Mostre como resultado se houve lucro, prejuízo ou empate para
# cada produto. Informe o valor de custo de cada produto, o valor de venda
# de cada produto, a média de preço de custo e do preço de venda;
for c in range(1,6):
    produto = str(input('Produto: '))
    custo = float(input('Preço de custo R$ '))
    venda = float(input('Preço de venda R$ '))
    resultado = venda - custo
    if venda > custo:
        print('Houve lucro de R${:.2f}'.format(resultado))
    elif venda == custo:
        print('Não houve nem lucro nem prejuízo.')
    else:
        print('Houve prejuízo de R${:.2f}'.format(resultado))
