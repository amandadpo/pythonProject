#Elabore um algoritmo que efetue a apresentação do valor da conversão
# em real (R$) de um valorlido em dólar (US$). O algoritmo deverá solicitar
# o valor da cotação do dólar e também aquantidade de dólares disponíveis
# com o usuário;
dolar = float(input('Digite a quantia em dólar US$ '))
cotação = float(input('Cotação do dólar US$ '))
valor = dolar * cotação
print('Você poderá comprar {:.2f} reais com {:.2f} dólares'.format(valor,dolar))
