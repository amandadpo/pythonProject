#Escreva um algoritmo que leia o nome de um vendedor, o seu salário fixo
# e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que
# este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar
# o seu nome, o salário fixo e salário no final do mês;
nome = str(input("Nome do vendedor: "))
salario = float(input("Salário fixo do vendedor: R$ "))
vendas = int(input("Total de vendas R$ "))
comissao = vendas * 0.15
novosalario = comissao + salario
print('Vendedor(a) {} tem o salário fixo de R${:.2f} e seu salário com comissão foi de R${:.2f}'.format(nome,salario,novosalario))
