# https://www.youtube.com/watch?v=mNjcrarT3Io&list=WL&index=21

import pygame
import random

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Meu jogo em Python")

bg = pygame.image.load('Jogos/bg.jpg').convert.alpha()
bg = pygame.transform.scale(bg, (x,y))

alien = pygame.image.load('Jogos/spaceship.png').convert.alpha()
alien = pygame.transform.scale()

vel_x_missil = 0
pos_x_missil = 200
pos_y_missil = 300

triggered = False

rodando = True

player_rect 

# Funções 
    def respawn ():
        x = 1350
        y = random.randint(1, 640)
        return[x,y]
    def respawn_missil():
        triggered == False
    
    def colision():
    
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    # teclas
    teca = pygame.key

    # Respawn
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn

    # Posição Rect 
    player_rect.y = pos_player_y
    player.rect.x = pos_player_x

    # Movimento
    x -= 2
    pos_alien_x -= 1
    pos_missil_x == vel_missil_x

    # Criar imagens
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playering, (pos_player_x, pos_player_y))
