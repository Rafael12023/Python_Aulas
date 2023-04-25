import pygame
#inicializando o mixer
pygame.mixer.init()

#iniciando o pygame
pygame.init()

#Reproduzindo
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0,start=0.0)
pygame.event.wait()

