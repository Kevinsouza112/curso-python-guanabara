# DESAFIO 05
# Objetivo: ler um numero inteiro e mostrar seu antecessor e sucessor.

# input() recebe o numero digitado pelo usuario como texto.
# int() converte esse texto para numero inteiro.
# O numero convertido fica guardado na variavel n.
n = int(input('Digite um numero: '))

# n - 1 calcula o numero que vem antes do valor digitado.
# format() coloca os valores de n e n - 1 dentro das chaves {} da frase.
print('O antecessor do {} e {}'.format(n, n - 1))

# n + 1 calcula o numero que vem depois do valor digitado.
# format() coloca os valores de n e n + 1 dentro das chaves {} da frase.
print('O sucessor do {} e {}'.format(n, n + 1))
