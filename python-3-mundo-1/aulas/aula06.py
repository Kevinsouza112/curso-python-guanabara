# AULA 06
# Objetivo: somar dois numeros inteiros digitados pelo usuario.

# input() recebe o primeiro valor como texto.
# int() converte esse texto para numero inteiro.
# O valor convertido fica guardado na variavel n1.
n1 = int(input('Digite um valor: '))

# input() recebe o segundo valor como texto.
# int() converte esse texto para numero inteiro.
# O valor convertido fica guardado na variavel n2.
n2 = int(input('Digite outro valor: '))

# O operador + soma os dois numeros inteiros.
# O resultado da soma fica guardado na variavel soma.
soma = n1 + n2

# print() mostra a frase final.
# format() coloca n1, n2 e soma dentro das chaves {}.
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
