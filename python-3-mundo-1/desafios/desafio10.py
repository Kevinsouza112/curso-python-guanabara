# DESAFIO 10
# Objetivo: converter dinheiro em reais para dolares usando uma cotacao fixa.

# print() mostra um titulo simples para identificar o desafio no terminal.
print('===== DESAFIO 010 =====')

# input() recebe o valor em reais como texto.
# float() converte esse texto para numero decimal.
# O valor convertido fica guardado na variavel dinheiro.
dinheiro = float(input('Quanto voce tem na carteira? R$ '))

# Guarda a cotacao fixa do dolar usada no exercicio.
dolar = 3.27

# Divide o dinheiro em reais pela cotacao para descobrir quantos dolares pode comprar.
resultado = dinheiro / dolar

# Mostra o valor em reais e o resultado em dolares com duas casas decimais.
print('Voce pode comprar com R$ {} \n{:.2f} dolares'.format(dinheiro, resultado))
