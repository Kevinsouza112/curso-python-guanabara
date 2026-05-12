# DESAFIO 16
# Objetivo: mostrar a parte inteira de um numero real.

# Importa a biblioteca math, que possui funcoes matematicas prontas.
import math

# input() recebe um numero decimal como texto.
# float() converte esse texto para numero real.
# O valor convertido fica guardado na variavel num.
num = float(input('Digite um numero quebrado para visualizar seu valor inteiro: '))

# math.trunc() remove a parte decimal do numero, mantendo apenas a parte inteira.
# format() encaixa o numero original e o resultado na frase.
print('O valor inteiro do {} e {}'.format(num, math.trunc(num)))
