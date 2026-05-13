# Faca um programa que leia o nome completo de uma pessoa
# e mostre o primeiro e o ultimo nome separadamente.
# Exemplo: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza

# Le o nome completo e remove espacos extras do inicio e do fim.
nome = input("Digite seu nome completo: ").strip()

# Separa o nome em partes, usando os espacos como divisao.
partes_do_nome = nome.split()

# Pega a primeira palavra da lista.
primeiro_nome = partes_do_nome[0]

# Pega a ultima palavra da lista.
ultimo_nome = partes_do_nome[-1]

# Mostra o primeiro nome encontrado.
print(f"Primeiro nome: {primeiro_nome}")

# Mostra o ultimo nome encontrado.
print(f"Ultimo nome: {ultimo_nome}")
