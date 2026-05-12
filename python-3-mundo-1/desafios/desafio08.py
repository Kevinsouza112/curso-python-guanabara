# DESAFIO 08
# Objetivo: converter uma medida em metros para centimetros e milimetros.

# print() mostra um titulo simples para identificar o desafio no terminal.
print('===== DESAFIO 008 =====')

# input() recebe a medida em metros como texto.
# float() converte esse texto para numero decimal.
# O valor convertido fica guardado na variavel n.
n = float(input('Digite um numero em metros: '))

# n * 100 converte metros para centimetros.
# n * 1000 converte metros para milimetros.
# format() encaixa os tres valores dentro da frase.
print('{} metros e igual a {} centimetros e igual a {} milimetros'.format(n, n * 100, n * 1000))
