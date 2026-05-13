# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "Silva" no nome.

# Le o nome completo e remove espacos extras do inicio e do fim.
nome = input("Digite seu nome completo: ").strip()

# Converte tudo para minusculas para encontrar "silva", "Silva" ou "SILVA".
nome_minusculo = nome.lower()

# Verifica se a palavra "silva" aparece em qualquer parte do nome.
tem_silva = "silva" in nome_minusculo

# Mostra True se encontrou "silva" e False se nao encontrou.
print(tem_silva)
