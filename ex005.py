n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
sub = n1-n2
m = n1*n2
d = n1/n2
e = n1**n2
r = s**(1/2)
di = n1//n2
print('A soma é {}, \n a subtração é {}, \n a multiplicação é {},\n a divisão é {}, \n'.format(s,sub,m,d), end=' ')
print ('A exponenciação é {}, \n a raiz quadrada é {:.3f} \n e a divisão inteira é {}'.format(e,r,di))

