#A concessionária de veículos “CARANGO” está vendendo os seus veículos
# com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e
# o valor a ser pago pelo cliente. O desconto deverá ser calculado sobre o
# valor do veículo de acordo com o combustível (álcool – 25%, gasolina – 21%
# ou diesel –14%). Com valor do veículo zero encerra entrada de dados.
# Informe total de desconto e total pago pelos clientes;
inicio = str(input('Digite [1] para iniciar o programa ou [0] para sair: '))
while inicio != 0:
    valor = float(input('Insira o valor do carro: '))
    combustivel = str(input('''Digite:
     [A] para Álcool
     [G] para Gasolina
     [D] para Diesel
     [0] para sair: ''')).upper().strip()[0]
    if combustivel == 'A':
        desconto1 = valor - (valor * 0.25)
        print('Você obteve um desconto de 25% e o valor do carro será R${}'.format(desconto1))
    elif combustivel == 'G':
        desconto2 = valor - (valor * 0.21)
        print('Você obteve um desconto de 21% e o valor do carro será de R${}'.format(desconto2))
    elif combustivel == 'D':
        desconto3 = valor - (valor * 0.14)
        print('VOcê obteve um desconto de 14% e o valor do carro será de R${}'.format(desconto3))
    else:
        print('FINALIZANDO...')
print('FIM')



