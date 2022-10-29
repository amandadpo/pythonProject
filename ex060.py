'''from math import factorial
n = int(input('Digite o número para ver o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))'''

n = int(input('Digite o número para ver o seu fatorial: '))
c = n
f = 1
print('{}! = '.format(n),end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else '=', end=' ')
    f *= c        # f = f * c
    c -= 1
print('{}'.format(f),end=' ')
