#A concessionária de veículos “CARANGO VELHO” está vendendo os seus
# veículos com desconto. Faça um algoritmo que calcule e exiba o valor
# do desconto e o valor a ser pago pelo cliente de vários carros.
# O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000
# - 12% e acima de 2000 - 7%. O sistema deverá perguntar se deseja continuar
# calculando desconto até que a resposta seja: “(N) Não”. Informar total de
# carros com ano até 2000 e total geral;
print('--- CONCESSIONÁRIA CARANGO VELHO ---')
condição = 'S'
contvelhos = 0
contnovos = 0
while condição == 'S':
    valor = float(input('Informe o valor do carro R$ '))
    ano = int(input('Informe o ano do carro: '))
    if ano <= 2000:
        desconto1 = valor - (valor * 0.12)
        print('O valor final com desconto será de R$ {:.2f}'.format(desconto1))
        contvelhos += 1
    else:
        desconto2 = valor - (valor * 0.07)
        print('O valor final com desconto será de R$ {:.2f}'.format(desconto2))
        contnovos += 1
    condição = str(input('Deseja continuar [S/N]: ')).upper().strip()
print('Foram exibidos {} carros com ano até 2000 e {} carros acima do ano 2000'.format(contvelhos,contnovos))








