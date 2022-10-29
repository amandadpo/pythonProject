#Escreva um algoritmo que leia o nome e o sexo de 56 pessoas e
# informe o nome e se ela é homem ou mulher. No final informe total
# de homens e de mulheres;
contf = 0
contm = 0
for c in range(1,7):
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Sexo [F/M]: ')).upper().strip()
    if sexo == 'F':
       contf += 1
    elif sexo == 'M':
        contm += 1
    else:
        print('Digite uma opção válida')
print('{} homens e {} mulheres'.format(contm,contf))



