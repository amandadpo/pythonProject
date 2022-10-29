#Faça um algoritmo que receba um valor que foi depositado e exiba o
# valor com rendimento após um mês.Considere fixo o juro da poupança
# em 0,07% a. m;
valor = float(input('Digite um valor que deseja investir: '))
mes = int(input('Digite a qtde de meses: '))
rendimento = (mes * 0.07) * valor + valor
print('O rendimento final de R$ {:.2f} em {} meses será R$ {:.2f}'.format(valor,mes,rendimento))


