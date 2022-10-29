#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
IMC = peso / (altura **2)
print('Seu IMC é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO!')
elif IMC < 25:
    print('Você está no peso ideal!')
elif IMC < 30:
    print('Você está em sobrepeso!')
elif IMC < 40:
    print('Você está em obesidade!')
else:
    print('Você está em obesidade mórbida!')
