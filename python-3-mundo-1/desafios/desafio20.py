# DESAFIO 20
# Objetivo: sortear a ordem de apresentacao de quatro alunos.

# Importa a biblioteca random, usada para trabalhar com sorteios e aleatoriedade.
import random

# input() recebe o primeiro nome digitado e guarda na variavel nome1.
nome1 = input('Digite seu nome: ')

# input() recebe o segundo nome digitado e guarda na variavel nome2.
nome2 = input('Digite seu nome: ')

# input() recebe o terceiro nome digitado e guarda na variavel nome3.
nome3 = input('Digite seu nome: ')

# input() recebe o quarto nome digitado e guarda na variavel nome4.
nome4 = input('Digite seu nome: ')

# Cria uma lista chamada nomes contendo os quatro nomes digitados.
nomes = [nome1, nome2, nome3, nome4]

# random.shuffle() embaralha a propria lista, mudando a ordem dos nomes.
random.shuffle(nomes)

# Mostra a lista ja embaralhada, representando a ordem sorteada.
print('Os nomes sorteados foram {}:'.format(nomes))
