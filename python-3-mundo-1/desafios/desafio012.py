print('===== DESAFIO 012 =====')
vproduto = float(input('Qual é o preço do produto? R$'))
desconto = vproduto * 5/100
novo_preco = vproduto - desconto

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(vproduto, novo_preco))
