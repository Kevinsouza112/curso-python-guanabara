# DESAFIO 17
# Objetivo: calcular a hipotenusa de um triangulo retangulo.

# Importa a biblioteca math, que possui funcoes matematicas prontas.
import math

# input() recebe o cateto oposto como texto.
# float() converte esse texto para numero decimal.
# O valor convertido fica guardado na variavel cateto_oposto.
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))

# input() recebe o cateto adjacente como texto.
# float() converte esse texto para numero decimal.
# O valor convertido fica guardado na variavel cateto_adjacente.
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

# math.hypot() calcula a hipotenusa usando os dois catetos.
# Essa funcao aplica o Teorema de Pitagoras internamente.
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# f-string permite colocar variaveis diretamente dentro do texto usando chaves.
# :.2f mostra a hipotenusa com duas casas decimais.
print(f'A hipotenusa mede: {hipotenusa:.2f}')

# Forma alternativa sem usar math.hypot():
# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5
