# DESAFIO 04
# Objetivo: analisar o que foi digitado pelo usuario usando metodos de string.

# input() recebe qualquer valor digitado pelo usuario.
# Mesmo que o usuario digite numeros, o Python guarda inicialmente como texto.
n = input('Digite algo: ')

# type() mostra qual e o tipo primitivo do valor digitado.
print('O tipo primitivo desse valor e', type(n))

# isspace() verifica se o texto possui apenas espacos.
print('So tem espacos?', n.isspace())

# isnumeric() verifica se o texto possui apenas caracteres numericos.
print('E um numero?', n.isnumeric())

# isalnum() verifica se o texto possui apenas letras e/ou numeros.
print('E alfanumerico?', n.isalnum())

# isalpha() verifica se o texto possui apenas letras.
print('E alfabetico?', n.isalpha())

# isupper() verifica se todas as letras estao em maiusculas.
print('Esta em maiusculas?', n.isupper())

# islower() verifica se todas as letras estao em minusculas.
print('Esta em minusculas?', n.islower())

# istitle() verifica se cada palavra comeca com letra maiuscula.
print('Esta capitalizado?', n.istitle())
