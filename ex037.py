#Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um número inteiro: '))
print('''[1] para converter para BINÁRIO
[2] para converter para OCTAL
[3] para converter para HEXADECIMAL''')
base = int(input('Digite sua escolha: '))
if base == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(numero,bin(numero)[2:]))
elif base == 2:
    print('O número {} convertido para OCTAL é {}'.format(numero,oct(numero)[2:]))
elif base == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(numero,hex(numero)[2:]))
else:
    print('Você digitou um número inválido')

