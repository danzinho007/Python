# https://www.youtube.com/watch?v=XcoDHTWJHYQ&list=PLzn2mIpnKXEo0iiFrlqv-fFAbRd0cjDLe&index=5&ab_channel=Guilhermeasper
# https://www.youtube.com/watch?v=yWNffL7YF_o&list=PLzn2mIpnKXEo0iiFrlqv-fFAbRd0cjDLe&index=8

#cloford.com = cores pro pyton 

# Objetivos :
# 01 = Configurar a janela do jogo
# 02 = Criar um evento que atualize a janela
# 03 = Pegar os comandos do teclado
# 04 = Criar a cobrinha
# 05 = Definindo cores
# 06 = Configurando teclas do teclado
# 07 = Configurando pra cobrinha começar em local aleatório
# 08 = Configurando movimento
# 09 = Definindo os frames pro segundo 
# 10 = Configurando bordas
# 11 = 

import pygame
from random import randint

white=(255,255,255) #Definindo cor branco
black=(0,0,0)
red=(255,0,0,)
green=(0,255,0)
blue=(0,0,255)

try:
    pygame.init()
except: 
    print("Erro")

width=640 #Largura
heigh=480 #Altura
size = 10
# pos_x = width/2 
pos_x = randint(0,(width-size)/10)*10
# pos_y = heigh/2
pos_y = randint(0,(heigh-size)/10)*10
speed_x=0
speed_y=0
clock = pygame.time.Clock()

background = pygame.display.set_mode((width,heigh)) #Janela do jogo
pygame.display.set_caption("Snake") #Título do jogo

sair = True
while sair: 
    for event in pygame.event.get(): #Pega os comandos do teclado
        if event.type == pygame.QUIT: #Quando clicar no X / apertar F4 o jogo vai sair
            sair = False
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_y=0
                speed_x=-size
                # pos_x-=10 # Pra esquerda é negativo
            if event.key == pygame.K_RIGHT:
                speed_y=0
                speed_x=size
                # pos_x+=10 # Pra direito é positivo
            if event.key == pygame.K_UP:
                speed_x=0
                speed_y=-size
                # pos_y-=10  # Pra cima é negativo
            if event.key == pygame.K_DOWN:
                speed_x=0
                speed_y=size
                # pos_y+=10  # Pra baixo é positivo
    background.fill(black)
    pygame.draw.rect(background, white, [pos_x,pos_y,size,size])
    pos_x+=speed_x
    pos_y+=speed_y
    pygame.display.update() #Atualiza a janela
    clock.tick(15) # Definindo os frames por segundo
    if pos_x > width:
        pos_x=0 # Se quiser que o jogo feche ao bater, só por sair = false
    if pos_x < 0 :
        pos_x=width - size # Se quiser que o jogo feche ao bater, só por sair = false
    if pos_y > heigh:
        pos_y = 0 # Se quiser que o jogo feche ao bater, só por sair = false
    if pos_y < 0 :
        pos_y= heigh - size # Se quiser que o jogo feche ao bater, só por sair = false
pygame.quit()
quit()

# Seleciona tudo e Alt + 3
# Seletiona tudo e Alt + 4
