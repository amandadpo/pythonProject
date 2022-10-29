#Crie um programa que leia vários números inteiros pelo teclado. No final
# da execução, mostre a média entre todos os valores e qual foi o maior e
# o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.
cont = soma = media = maior = menor = 0
r = "S"
while r in "S":
    n = int(input("Digite um valor: "))
    cont += 1
    soma += n
    r = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media += soma/cont
print('Foram exibidos {} números e a média entre eles é {:.2f}.'.format(cont,media))
print('O maior número digitado é {} e o menor número digitado é {}'.format(maior,menor))
print('FIM')