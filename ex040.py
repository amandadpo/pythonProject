#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Sua média foi {:.2f} e você está \33[31mREPROVADO\33[m!'.format(media))
elif 7 > media >=5:
    print('Sua média foi {:.2f} e você está em \33[33mRECUPERAÇÃO\33[m!'.format(media))
else:
    print('Sua média foi {:.2f} e você está \33[34mAPROVADO\33[m!'.format(media))

