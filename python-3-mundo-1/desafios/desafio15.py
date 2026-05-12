# DESAFIO 15
# Objetivo: calcular o preco do aluguel de um carro.

# input() recebe a quantidade de dias como texto.
# int() converte esse texto para numero inteiro.
# O valor convertido fica guardado na variavel dias.
dias = int(input('Quantos dias alugados? '))

# input() recebe a quantidade de quilometros rodados como texto.
# float() converte esse texto para numero decimal.
# O valor convertido fica guardado na variavel km.
km = float(input('Quantos Km rodados? '))

# Calcula o total: R$60 por dia mais R$0.15 por quilometro rodado.
pago = (dias * 60) + (km * 0.15)

# Mostra o total a pagar com duas casas decimais.
print('O total a pagar e de {:.2f}'.format(pago))
