# DESAFIO 13
# Objetivo: calcular um aumento de 15% no salario.

# input() recebe o salario como texto.
# float() converte esse texto para numero decimal.
# O salario convertido fica guardado na variavel salario.
salario = float(input('Digite seu salario: '))

# Multiplica o salario por 15/100 para calcular o valor do aumento.
aumento = salario * 15 / 100

# Soma o salario original com o aumento para obter o novo salario.
novo_salario = salario + aumento

# Mostra o novo salario com duas casas decimais.
print('Seu salario teve um aumento de 15% e o valor dele agora passara para {:.2f}'.format(novo_salario))
