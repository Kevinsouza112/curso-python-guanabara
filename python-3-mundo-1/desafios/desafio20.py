import random

nome1= input("Digite seu nome: ")
nome2= input("Digite seu nome: ")
nome3= input("Digite seu nome: ")
nome4= input("Digite seu nome: ")

nomes=[nome1, nome2, nome3, nome4]

random.shuffle(nomes)

print('Os nomes sorteados foram {} :'.format(nomes))