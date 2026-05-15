# AULA 07
# Objetivo: praticar operadores aritmeticos em Python.

# input() recebe o primeiro numero como texto.
# int() converte esse texto para numero inteiro.
# O valor convertido fica guardado na variavel n1.
n1 = int(input('Digite um numero: '))

# input() recebe o segundo numero como texto.
# int() converte esse texto para numero inteiro.
# O valor convertido fica guardado na variavel n2.
n2 = int(input('Digite outro numero: '))

# O operador + soma n1 e n2.
s = n1 + n2

# O operador * multiplica n1 por n2.
m = n1 * n2

# O operador / faz a divisao real, ou seja, pode gerar resultado decimal.
d = n1 / n2

# O operador // faz a divisao inteira, descartando a parte decimal.
di = n1 // n2

# O operador ** calcula a potencia, ou seja, n1 elevado a n2.
e = n1 ** n2

# Mostra soma, multiplicacao e divisao real.
# {:.3f} mostra a divisao com tres casas decimais.
print('A soma e {}, A multiplicacao e {}, A divisao e {:.3f}'.format(s, m, d))

# Mostra a divisao inteira e a potencia.
print('A divisao inteira e {}, A potencia e {}'.format(di, e))
