#Elabore um algoritmo que efetue a apresentação do valor da conversão
# em real (R$) de um valorlido em dólar (US$). O algoritmo deverá solicitar
# o valor da cotação do dólar e também aquantidade de dólares disponíveis com
# ousuário;
dolar = float(input('Digite o valor em dolar US$ '))
cotacao = float(input('Digite a cotação do dolar R$ '))
real = dolar * cotacao
print('COm a quantia de US$ {:.2f} você poderá comprar R$ {:.2f}'.format(dolar,real))