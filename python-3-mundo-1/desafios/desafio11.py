largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
tinta = area / 2

print('A altura da sua parede é {:.2f} e a largura é {:.2f}'.format(altura,largura))
print('O total da area é de {:.2f}m² e será necessaria {:.2f}L de tinta para pintar'.format(area, tinta))