# Executar com F5

#21- Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3

import pygame
pygame.init()
pygame.mixer.music.load('ex031.mp3')
pygame.mixer.music.play()
pygame.event.wait()
