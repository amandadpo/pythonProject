#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = atual - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Tivemos {} pessoas maiores de idade'.format(totmaior))
print('E {} menores de idade'.format(totmenor))








