# AULA 06B
# Objetivo: verificar se o valor digitado possui apenas caracteres numericos.

# input() recebe qualquer coisa digitada pelo usuario e guarda como texto.
n = input('Digite algo: ')

# isnumeric() retorna True se o texto tiver apenas caracteres numericos.
# Caso contrario, retorna False.
print(n.isnumeric())
