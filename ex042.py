#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo: ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or b == c or c == a:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Não é possível formar um triângulo!')




