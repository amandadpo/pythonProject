#Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. Pergunte o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
# do salário ou então o empréstimo será negado.
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Informe em quantos anos pretende pagar as prestações: '))
prestação = casa / (anos * 12)
if prestação <= (salario * 0.30):
    print('Empréstimo concedido! O valor da sua prestação será R${:.2f} em {} anos'.format(prestação,anos))
else:
    print('O empréstimo foi negado.')