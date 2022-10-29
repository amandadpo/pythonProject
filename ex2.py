#Faça um algoritmo que receba dois números e ao final mostre a soma,
# subtração, multiplicação e a divisão dos dois números lidos;
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
sub = n1 - n2
multip = n1 * n2
div = n1 / n2
print('''Cálculos: 
Soma: {} 
Subtração: {}
Multiplicação: {}
Divisão: {}'''.format(soma,sub,multip,div))

