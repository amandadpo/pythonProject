produto = float(input('Digite o valor do produto:R$ '))
desconto = produto-(produto*0.05)
print('O valor do produto com 5% de desconto é: R$ {:.2f}'.format(desconto))
print('-'* 20)
produto = float(input('Digite o valor do produto:R$ '))
desconto = produto-(produto*0.10)
aumento = produto+(produto*0.10)
print('Pagamento à vista com desconto de 10% = R${:.2f} \nPagamento à prazo com acréscimo de 10% = R${:.2f}'.format(desconto,aumento))