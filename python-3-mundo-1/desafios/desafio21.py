import pygame
import time
pygame.init()
pygame.mixer.music.load('desafios/desafio21.wav')
pygame.mixer.music.play()

print("Áudio iniciado. Tocando desafio21.wav...")
time.sleep(60)
pygame.quit()