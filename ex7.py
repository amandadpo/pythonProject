#Leia uma temperatura em graus Celsius e apresentá-la convertida em
# graus Fahrenheit. Afórmula de conversão é:F=(9*C+160) / 5, sendo F
# a temperatura em Fahrenheit e C a temperatura em Celsius;
c = float(input('Temperatura em ºC: '))
F = (9*c+160)/5
print('A temperatura {}Cº convertida em Fahrenheit é {:.2f}Fº'.format(c,F))


