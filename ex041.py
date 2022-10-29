#A Confederação Nacional de Natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.
ano = int(input('Informe o ano de nascimento: '))
from datetime import date
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('O atleta tem {} anos e sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e sua categoria é JÚNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e sua categoria é SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos e sua categoria é MASTER'.format(idade))
