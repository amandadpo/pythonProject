n = input('Digite algo: ')
print('\33[4;37;40mÉ alfanumérico?\33[m',(n.isalnum()))
print('\33[0;31mÉ alfabético?\33[m',(n.isalpha()))
print('\33[1;34mÉ numérico?\33[m',(n.isnumeric()))
print('\33[1;36mEstá minúsculo?\33[m',(n.islower()))
print('\33[1;33mEstá maiúsculo?\33[m',(n.isupper()))
print('\33[4;31;42mÉ decimal?\33[m',(n.isdecimal()))
print('\33[1;7;30mEstá capitalizada?\33[m',(n.istitle())) #Primeira maiúscula e o resto minúsculo