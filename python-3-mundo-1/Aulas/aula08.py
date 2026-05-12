# AULA 08
# Objetivo: usar a biblioteca math para calcular raiz quadrada.

# Importa a biblioteca math, que possui funcoes matematicas prontas.
import math

# Exemplo alternativo:
# num = int(input('Digite um numero: '))
# raiz = math.sqrt(num)
# math.ceil(raiz) arredondaria a raiz para cima.
# print('A raiz de {} e igual {}'.format(num, math.ceil(raiz)))

# input() recebe um numero como texto.
# int() converte esse texto para numero inteiro.
# O valor convertido fica guardado na variavel num.
num = int(input('Digite um numero: '))

# math.sqrt() calcula a raiz quadrada do numero.
# O resultado fica guardado na variavel raiz.
raiz = math.sqrt(num)

# math.floor() arredonda o resultado para baixo.
# format() encaixa o numero original e a raiz arredondada dentro da frase.
print('A raiz de {} e igual {}'.format(num, math.floor(raiz)))
