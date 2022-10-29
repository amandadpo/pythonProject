nome = str(input('Digite seu nome completo: ')).strip() #eliminar os espaços antes e depois
print('Seu nome minúsculo: {}'.format(nome.lower()))
print('Seu nome maiúsculo: {}'.format(nome.upper()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))


