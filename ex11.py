#Faça um algoritmo que receba o preço de custo de um produto e mostre
# o valor de venda. Sabe-se que o preço de custo receberá um acréscimo
# de acordo com um percentual informado pelo usuário;
custo = float(input('Informe o custo do produto: '))
percentual = float(input('Informe o percentual de lucro(%): '))
conversao = percentual/100
venda = (custo * conversao) + custo
print('O valor de venda é R$ {:.2f}'.format(venda))