#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer
# mostrar 0 termos.
print('Termos de uma PA')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -'.format(termo), end=' ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja ver mais quantos termos? '))
print('FIM')

