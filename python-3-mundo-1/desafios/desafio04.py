# DESAFIO 04
# Objetivo: analisar o que foi digitado pelo usuario usando metodos de string.

# input() recebe qualquer valor digitado pelo usuario.
# Mesmo que o usuario digite numeros, o Python guarda inicialmente como texto.
n = input('Digite algo: ')

# isnumeric() verifica se o texto possui apenas caracteres numericos.
print(n.isnumeric())

# isalnum() verifica se o texto possui apenas letras e/ou numeros.
print(n.isalnum())

# isalpha() verifica se o texto possui apenas letras.
print(n.isalpha())

# isascii() verifica se todos os caracteres fazem parte da tabela ASCII.
print(n.isascii())

# isdecimal() verifica se o texto possui apenas numeros decimais simples.
print(n.isdecimal())

# isdigit() verifica se o texto possui apenas digitos.
print(n.isdigit())
