# Faca um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra A
# - Em que posicao ela aparece pela primeira vez
# - Em que posicao ela aparece pela ultima vez

# Le a frase digitada e remove espacos extras do inicio e do fim.
frase = input("Digite uma frase: ").strip()

# Converte a frase para minusculas para contar "a" e "A" do mesmo jeito.
frase_minuscula = frase.lower()

# Conta quantas vezes a letra "a" aparece na frase.
quantidade_de_a = frase_minuscula.count("a")

# Encontra a primeira posicao em que a letra "a" aparece.
primeira_posicao = frase_minuscula.find("a")

# Encontra a ultima posicao em que a letra "a" aparece.
ultima_posicao = frase_minuscula.rfind("a")

# Mostra a quantidade de letras "a" encontradas.
print(f"A letra A aparece {quantidade_de_a} vezes.")

# Mostra as posicoes no padrao do Python, em que a contagem comeca em 0.
print(f"A primeira letra A aparece na posicao {primeira_posicao}.")
print(f"A ultima letra A aparece na posicao {ultima_posicao}.")
