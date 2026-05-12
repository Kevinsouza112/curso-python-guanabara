# DESAFIO 18
# Objetivo: calcular seno, cosseno e tangente de um angulo.

# Importa a biblioteca math, que possui funcoes matematicas prontas.
import math

# input() recebe o angulo em graus como texto.
# int() converte esse texto para numero inteiro.
# O valor convertido fica guardado na variavel angulo.
angulo = int(input('Digite um angulo para saber o Seno, Cosseno e Tangente: '))

# As funcoes sin(), cos() e tan() trabalham com radianos.
# math.radians() converte o angulo de graus para radianos.
angulo_rad = math.radians(angulo)

# math.sin() calcula o seno do angulo em radianos.
# {:.3f} mostra o resultado com tres casas decimais.
print('O seno de {} e igual a {:.3f}'.format(angulo, math.sin(angulo_rad)))

# math.cos() calcula o cosseno do angulo em radianos.
# {:.3f} mostra o resultado com tres casas decimais.
print('O cosseno de {} e igual a {:.3f}'.format(angulo, math.cos(angulo_rad)))

# math.tan() calcula a tangente do angulo em radianos.
# {:.3f} mostra o resultado com tres casas decimais.
print('A tangente de {} e igual a {:.3f}'.format(angulo, math.tan(angulo_rad)))
