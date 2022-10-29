salario = float(input('Digite o salário do funcionário: '))
aumento_salarial = (salario*0.15)+salario
print('Seu novo salário com aumento de 15% é R$ {:.2f}'.format(aumento_salarial))
print('-'* 30)
salario = float(input('Digite o valor do salário R$ '))
desconto_planodesaude = salario-(salario*0.20)
print('Salário com desconto de 20% do plano de saúde é:R${}'.format(desconto_planodesaude))