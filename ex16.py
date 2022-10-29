#Escreva um algoritmo que leia o nome e as três notas obtidas por um
# aluno durante o semestre. Calcular a sua média (aritmética), informar
# o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5) e
# Recuperação (media entre 5.1 a 6.9);
aluno = str(input('Nome do aluno: '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1+n2+n3)/3
if media >= 7:
    print('O aluno {} obteve media {:.2f} no semestre e sua condição é APROVADO.'.format(aluno,media))
elif media > 5 and media < 7:
   print('O aluno {} obteve média {:.2f} no semestre e sua condição é RECUPERAÇÂO'.format(aluno,media))
else:
    print('O aluno {} obteve média {:.2f} no semestre e sua condição é REPROVADO'.format(aluno,media))

