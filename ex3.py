#Escreva um algoritmo que leia o nome de um aluno e as notas das três
# provas que ele obteve no semestre. No final informar o nome do aluno e
# a sua média (aritmética);
aluno = str(input('Nome do aluno: '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1+n2+n3)/3
print('O aluno {} obteve a média {} no semestre.'.format(aluno,media))

