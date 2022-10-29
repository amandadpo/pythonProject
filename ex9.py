#Faça um algoritmo que receba um valor que foi depositado e exiba o
# valor com rendimento após um mês.Considere fixo o juro da poupança em
# 0,07% a. m;
print('Calculadora de rendimentos')
print('='* 20)
valor = int(input('Valor depositado R$ '))
mes = int(input('Informe por quantos meses: '))
rendimento = ((mes * 0.07) * valor) + valor
print('Ao final de {} meses você terá um rendimento de R$ {:.2f}'.format(mes,rendimento))

