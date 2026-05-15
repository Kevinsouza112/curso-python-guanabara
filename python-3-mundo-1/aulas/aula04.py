# AULA 04
# Objetivo: praticar entrada de dados com input() e saida com print().

# input() mostra a pergunta na tela e espera o usuario digitar uma resposta.
# O texto digitado fica guardado na variavel nome.
nome = input('Qual seu nome? ')

# input() le a idade digitada pelo usuario.
# Como nao usamos int(), a idade fica guardada como texto.
idade = input('Qual sua idade? ')

# input() le o peso digitado pelo usuario.
# Como nao usamos float(), o peso tambem fica guardado como texto.
peso = input('Qual seu peso? ')

# print() mostra na tela os tres valores guardados nas variaveis.
print(nome, idade, peso)
