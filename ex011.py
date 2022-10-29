altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura*largura
tinta = area/2
print('A área da parede é: {}m² e será necessário {:.1f} litro(s) de tinta para pintá-la.'.format(area,tinta))
