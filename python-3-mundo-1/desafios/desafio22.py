# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiusculas
# - O nome com todas as letras minusculas
# - Quantas letras ao todo, sem considerar espacos
# - Quantas letras tem o primeiro nome

# Le o nome completo digitado e remove espacos extras do inicio e do fim.
nome_completo = input("Digite seu nome completo: ").strip()

# Mostra o nome inteiro em letras maiusculas.
print(f"Maiusculas: {nome_completo.upper()}")

# Mostra o nome inteiro em letras minusculas.
print(f"Minusculas: {nome_completo.lower()}")

# Remove todos os espacos entre as palavras para contar apenas letras.
nome_sem_espacos = nome_completo.replace(" ", "")

# Mostra a quantidade de letras do nome completo, sem contar espacos.
print(f"Quantidade de letras sem espacos: {len(nome_sem_espacos)}")

# Separa o nome completo em uma lista de palavras.
partes_do_nome = nome_completo.split()

# Mostra quantas letras tem a primeira palavra do nome.
print(f"Letras do primeiro nome: {len(partes_do_nome[0])}")
