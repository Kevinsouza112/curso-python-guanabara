# DESAFIO 21
# Objetivo: tocar um arquivo de audio usando a biblioteca pygame.

# Importa a biblioteca pygame, usada aqui para carregar e tocar audio.
import pygame

# Importa Path para montar o caminho do arquivo de audio.
from pathlib import Path

# Importa a biblioteca time, usada aqui para pausar o programa por alguns segundos.
import time

# Guarda o caminho do arquivo de audio que esta na mesma pasta deste programa.
audio = Path(__file__).with_name('desafio21.wav')

# Inicializa os modulos do pygame para que o mixer de audio possa ser usado.
pygame.init()

# Carrega o arquivo de audio que sera tocado.
pygame.mixer.music.load(audio)

# Inicia a reproducao do audio carregado.
pygame.mixer.music.play()

# Mostra uma mensagem avisando que o audio comecou a tocar.
print('Audio iniciado. Tocando desafio21.wav...')

# Mantem o programa aberto por 60 segundos para dar tempo de o audio tocar.
time.sleep(60)

# Encerra os modulos do pygame ao final do programa.
pygame.quit()
