import math
angulo = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O angulo {}, tem o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(angulo,sen,cos,tang))
