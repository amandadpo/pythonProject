cateto_oposto = float(input('Informe cateto oposto: '))
cateto_adjacente = float(input('Informa cateto adjacente: '))
hipotenusa = (cateto_oposto**2 + cateto_adjacente**2) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))

import math
co = float(input('Digite cateto oposto: '))
ca = float(input('Digite cateto adjacente: '))
hi = math.hypot(co,ca)
print('O comprimento da hipotenusa é: {:.2f}'.format(hi))