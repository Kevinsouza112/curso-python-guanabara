# DESAFIO 19
# Objetivo: sortear um nome entre quatro alunos.

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

# random.choice() escolhe aleatoriamente um item da lista nomes.
sorteado = random.choice(nomes)

# Mostra o nome que foi sorteado.
print('O nome sorteado foi {}'.format(sorteado))
