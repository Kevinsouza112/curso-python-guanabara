# DESAFIO 11
# Objetivo: calcular a area de uma parede e a quantidade de tinta necessaria.

# input() recebe a largura como texto.
# float() converte esse texto para numero decimal.
# A largura convertida fica guardada na variavel largura.
largura = float(input('Qual a largura da parede: '))

# input() recebe a altura como texto.
# float() converte esse texto para numero decimal.
# A altura convertida fica guardada na variavel altura.
altura = float(input('Qual a altura da parede: '))

# Multiplica largura por altura para calcular a area da parede.
area = largura * altura

# Divide a area por 2 porque, neste exercicio, 1 litro de tinta pinta 2 metros quadrados.
tinta = area / 2

# Mostra altura e largura com duas casas decimais.
print('A altura da sua parede e {:.2f} e a largura e {:.2f}'.format(altura, largura))

# Mostra a area e a quantidade de tinta necessaria com duas casas decimais.
print('O total da area e de {:.2f}m2 e sera necessaria {:.2f}L de tinta para pintar'.format(area, tinta))
