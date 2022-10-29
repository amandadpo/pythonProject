#Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite o valor do salário R$ '))
if salario > 1250:
    salario1 = (salario*0.10)+salario
    print('Seu salário com aumento de 10% foi para R$ {:.2f}'.format(salario1))
else:
    s2 = (salario*0.15)+salario
    print('Seu salário com aumento de 15% foi para R$ {:.2f}'.format(s2))

