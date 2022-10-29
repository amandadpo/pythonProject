#Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até
# ter um valor correto.
sexo = str(input('Digite sexo [F] para Feminino e [M] para marculino: ')).upper().strip()[0]
while sexo not in "FM":
    sexo = str(input('Digite uma opção válida: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))




