# 1- Importar a biblioteca pygame
# 2- Inicializar o pygame
# 3- Configurar a janela
# 4- Define cores
# 5- Cria um loop
# 6- Encerra o game

import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600  # Tamanho da janela
tela = pygame.display.set_mode((largura, altura))  # Cria a janela
pygame.display.set_caption("Aula 01")

# Cores (RGB)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela
            rodando = False

    # Desenhando formas
    pygame.draw.line(tela, vermelho, (50, 50), (200, 50), 5)  # Linha (tela, cor, início, fim, espessura)
    pygame.draw.rect(tela, verde, (100, 100, 150, 80))  # Retângulo (tela, cor, [x, y, largura, altura])
    pygame.draw.circle(tela, azul, (400, 300), 50)  # Círculo (tela, cor, centro, raio)
    pygame.draw.ellipse(tela, branco, (300, 400, 200, 100))  # Elipse (tela, cor, [x, y, largura, altura])

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
