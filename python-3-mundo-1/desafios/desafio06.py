# DESAFIO 06
# Objetivo: ler um numero e mostrar o dobro, o triplo e a raiz quadrada.

# print() mostra um titulo simples para identificar o desafio no terminal.
print('===== DESAFIO 006 =====')

# input() recebe o numero digitado como texto.
# int() converte esse texto para inteiro e guarda na variavel n.
n = int(input('Digite um numero: '))

# Multiplica n por 2 para calcular o dobro.
dobro = n * 2

# Multiplica n por 3 para calcular o triplo.
triplo = n * 3

# Eleva n a potencia 0.5, que equivale a calcular a raiz quadrada.
raiz = n ** 0.5

# Mostra o dobro do numero usando format() para encaixar os valores na frase.
print('O dobro do {} e {}'.format(n, dobro))

# Mostra o triplo do numero usando format().
print('O triplo do {} e {}'.format(n, triplo))

# Mostra a raiz quadrada com duas casas decimais usando {:.2f}.
print('A raiz quadrada de {} e {:.2f}'.format(n, raiz))
