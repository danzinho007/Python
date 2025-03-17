import pygame
# Inicializar o Pygame
pygame.init()
# Carregar a imagem
imagem = pygame.image.load("Python/Jogos/Field1.png")
imagem1 = pygame.image.load("Python/Jogos/n1.jpg")
# Pegar as dimensões da imagem
largura, altura = imagem.get_size()
# Criar a janela com o tamanho exato da imagem
screen = pygame.display.set_mode((largura, altura))
# Contador de pressionamento de ESC
esc_pressionado = 0  
# Posição inicial da imagem
# Campo : 
# Deck   1,2,3 Damage
# Drop   4,5,6 Zone
#          7
# Damage 1,2,3 Deck
# Zone   4,5,6 Drop
# x + direita
# x - esquerda
# y + desce
# y - sobe
x, y = 168, 209
# 130, 20 -
# 100,200 - 200,200 -
# 200,300 -         -
# 130,450 -         - 400,440
# 200,600 -         -
# Nova posição ao mover imagem
nova_x1, nova_y1 = 130, 450
nova_x2, nova_y2 = 130, 20
# Do 3 jogador pro 1 jogador
min_x1, max_x1 = 400, 479
min_y1, max_y1 = 450, 537
# Do 1 jogador pro 1 oponente
min_x2, max_x2 = 120, 215
min_y2, max_y2 =  20, 130
# Exibir texto
font = pygame.font.SysFont('Arial', 24)
# Armazenas posição do mouse
mouse_x, mouse_y = 0,0

# Loop Principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
            if evento.key == pygame.K_ESCAPE:  # Se for ESC
                esc_pressionado += 1  
                if esc_pressionado >= 2:  # Se ESC foi pressionado 2 vezes
                    rodando = False
            else:
                esc_pressionado = 0  # Reseta se outra tecla for pressionada
# Se clicar vai pegar a largura e altura da imagem :
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = evento.pos
            largura_img, altura_img = imagem.get_size()
# Verifica se o clique foi dentro da imagem
# + Move a imagem 
            if min_x1 <= mouse_x <= min_x1 and min_y1 <= mouse_y <= max_y1:
                x, y = nova_x1, nova_y1  
# Verifica se o clique foi dentro da imagem
# + Move a imagem 
            if min_x2 <= mouse_x <= max_x2 and min_y2 <= mouse_y <= max_y2:
                x, y = nova_x2, nova_y2
# Verificar se o clique foi com o botão direito
            if evento.button == 3:
                x, y = 400, 440
# Desenhar a imagem na tela
    screen.blit(imagem,  (0, 0))
    screen.blit(imagem1, (x, y))
# Criar texto com as coordenadas do clique : 
    texto = font.render(f'Posição do clique: ({mouse_x}, {mouse_y})', True, (0, 0, 0))
# Desenhar o texto na tela
    screen.blit(texto, (10, 10))  # Ajuste da posição onde o texto será mostrado
# Atualizar a tela
    pygame.display.flip()
# Finalizar o Pygame
pygame.quit()

#1-Energia x15 
#2-Armadura x5
#3-Energia x15
#4-Chave Azul x1
#5-Chave Vermelha x1
#6-Energia x15
#7-Moeda 4h
#8-Armadura x5
#9-Chave Azul x1
#10-Chave Vermelha x1
#11-Energia x15
#12-Moeda 4h
#13-Armadura x5
#14-Chave Azul x1
#15-Chave Vermelha x1
#16-Energia x15
#20-Chave Mestra x1
#30-Chave Mestra x1