# DESAFIO 12
# Objetivo: calcular o preco de um produto com 5% de desconto.

# print() mostra um titulo simples para identificar o desafio no terminal.
print('===== DESAFIO 012 =====')

# input() recebe o preco do produto como texto.
# float() converte esse texto para numero decimal.
# O preco convertido fica guardado na variavel vproduto.
vproduto = float(input('Qual e o preco do produto? R$ '))

# Multiplica o preco por 5/100 para calcular 5% do valor.
desconto = vproduto * 5 / 100

# Subtrai o desconto do preco original para obter o novo preco.
novo_preco = vproduto - desconto

# Mostra o preco antigo e o preco com desconto, ambos com duas casas decimais.
print('O produto que custava R${:.2f}, na promocao com desconto de 5% vai custar R${:.2f}'.format(vproduto, novo_preco))
