# 1 - Importar bibliotecas
# 2 - Inicializar o Pygame
# 3 - Configurar o jogo ( largura, altura e FPS )
# 4 - Criar o loop principal
# 5 - 

import pygame
from pygame.locals import *
from sys import exit

# Inicilizar o Pygame
pygame.init()

#Configuração do jogo
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sokoban com Teletransporte')

# Loop Principal
while True :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    # Desenhando um retângulo na tela com :
    # cor R,G,B = 0,0,255 > Azul
    # posição x,y,largura, altura = 200,300,40,50
    pygame.draw.rect(tela, (0,0,255), (200,300,40,50))
    # pygame.draw.circle(tela, (0,255,0), (300,260), 40)
    # pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5)
    pygame.display.update()

# "#" Parede
# "T" Teletransprote
# "%" Caixa
# "." Objetivo
# " " Chão
# "+" Jogador sobre o objetivo
# "*" Caixa sobre o objetivo
