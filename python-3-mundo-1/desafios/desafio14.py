# DESAFIO 14
# Objetivo: converter uma temperatura de Celsius para Fahrenheit.

# input() recebe a temperatura em Celsius como texto.
# float() converte esse texto para numero decimal.
# O valor convertido fica guardado na variavel c.
c = float(input('Informe a temperatura em C: '))

# Aplica a formula de conversao: F = (9 * C / 5) + 32.
f = ((9 * c) / 5) + 32

# Mostra a temperatura em Celsius e o valor correspondente em Fahrenheit.
print('A temperatura de {}C corresponde a {}F'.format(c, f))
