# Crie um programa que leia o nome de uma cidade
# e diga se ela comeca ou nao com o nome "Santo".

# Le o nome da cidade e remove espacos extras do inicio e do fim.
cidade = input("Digite o nome da cidade: ").strip()

# Converte para minusculas antes de comparar, evitando erro com "Santo" ou "santo".
cidade_minuscula = cidade.lower()

# Verifica se o texto comeca exatamente com "santo".
comeca_com_santo = cidade_minuscula.startswith("santo")

# Mostra True se comecar com "santo" e False se nao comecar.
print(comeca_com_santo)
