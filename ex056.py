#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome
# do homem mais velho e quantas mulheres têm menos de 20 anos.
maisvelho = 0
nomemaisvelho = ''
media = 0
cont = 0
for c in range(1,5):
    nome = str(input('Digite nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = int(input('Digite [1] para sexo masculino e [2] para sexo feminino: '))
    media += idade / 4
    if c == 1 and sexo == 1:
        maisvelho = idade
        nomemaisvelho = nome
    else:
        if idade > maisvelho:
            maisvelho = idade
            nomemaisvelho = nome
    if sexo == 2 and idade < 20:
        cont += 1
print('A média da idades é {:.1f}'.format(media))
print('A idade do homem mais velho é {} e seu nome é {}'.format(maisvelho,nomemaisvelho))
print('Ao todo {} mulheres tem menos de 20 anos'.format(cont))


