# DESAFIO 03
# Objetivo: ler dois numeros inteiros, somar e mostrar o resultado.

# input() recebe o primeiro numero como texto.
# int() converte esse texto para numero inteiro, permitindo fazer contas.
# O resultado convertido fica guardado na variavel num1.
num1 = int(input('Digite um numero: '))

# input() recebe o segundo numero como texto.
# int() converte esse texto para inteiro e guarda na variavel num2.
num2 = int(input('Digite outro numero: '))

# O operador + soma os dois numeros guardados nas variaveis.
# O resultado da soma fica guardado na variavel soma.
soma = num1 + num2

# print() mostra o texto e o valor calculado da variavel soma.
print('A soma dos numeros e', soma)
