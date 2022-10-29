#Leia 80 números e ao final informar quantos número(s) est(á)ão no
# intervalo entre 10 (inclusive) e 150 (inclusive);
cont = 0
for c in range(1,6):
    num = int(input('Informe o valor: '))
    if num >= 10 and num <= 150:
        cont = cont + 1
print('{} números estão no intervalo'.format(cont))
