nome = input("Qual é o seu nome?")
print('É um prazer te conhecer \33[0;35m{}\33[m!'.format(nome))
n1 = int(input("Escolha um número: "))
n2 = int(input("Escolha mais um número: "))
soma = n1 + n2
#print("A soma de", n1, 'com', n2, 'é', soma)
print('A soma entre \33[1;32m{}\33[m e \33[7;30m{}\33[m é igual a \33[33m{}\33[m'.format(n1, n2, soma))

