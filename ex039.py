#Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
data = int(input('Informe o ano do seu nascimento: '))
sexo = int(input('''Digite: 
[1] para o sexo masculino ou [2] para o sexo feminino: '''))
from datetime import date
ano = date.today().year
n = ano - data
if n == 18 and sexo == 1:
    print('Você tem {} anos e deve se alistar!'.format(n))
elif n < 18 and sexo == 1:
    print('Você tem {} anos e ainda faltam {} anos para o seu alistamento. \n'
          'Seu alistamento será em {}'.format(n,18-n,data+18))
elif n > 18 and sexo == 1:
    print('Você tem {} anos e já se passaram {} anos do seu alistamento. \n'
          'Seu alistamento foi no ano de {}'.format(n,n-18,data+18))
else:
    print('Você é mulher e não precisa se alistar!')