# DESAFIO 21
# Objetivo: tocar um arquivo de audio usando a biblioteca pygame.

# Importa a biblioteca pygame, usada aqui para carregar e tocar audio.
import pygame

# Importa a biblioteca time, usada aqui para pausar o programa por alguns segundos.
import time

# Inicializa os modulos do pygame para que o mixer de audio possa ser usado.
pygame.init()

# Carrega o arquivo de audio que sera tocado.
pygame.mixer.music.load('desafios/desafio21.wav')

# Inicia a reproducao do audio carregado.
pygame.mixer.music.play()

# Mostra uma mensagem avisando que o audio comecou a tocar.
print('Audio iniciado. Tocando desafio21.wav...')

# Mantem o programa aberto por 60 segundos para dar tempo de o audio tocar.
time.sleep(60)

# Encerra os modulos do pygame ao final do programa.
pygame.quit()
