#Escreva um algoritmo que leia os dados de “N” pessoas (nome, sexo,
# idade e saúde) e informe se está apta ou não para cumprir o serviço
# militar obrigatório. Informe os totais;
condicao = 'S'
contapto = continapto = contmulher = 0
while condicao == 'S':
    nome = str(input('Nome do candidato: ')).upper().strip()
    sexo = str(input('Sexo [F/M]: ')).upper().strip()
    idade = int(input('Idade: '))
    saude = str(input('Inspeção de saúde [APTO/INAPTO]: ')).upper().strip()
    if sexo == 'M' and idade == 18 and saude == 'APTO':
        print('Candidato {}, está APTO a cumprir o serviço militar obrigatório!'.format(nome))
        contapto += 1
    elif sexo == 'F':
        print('Candidata MULHER. Não é obrigatório o serviço militar!')
        contmulher += 1
    else:
        print('Candidato {}, está INAPTO a cumprir o serviço militar obrigatório.'.format(nome))
        continapto += 1
    condicao = str(input('Deseja cadastrar mais candidatos [S/N]? ')).upper().strip()
print('Foram cadastrados {} aptos, {} inaptos e {} mulheres.'.format(contapto,continapto,contmulher))
print('FIM')


