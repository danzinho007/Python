import numpy as np
import pygame
import sys
import tensorflow as tf

class PongGame:
    def __init__(self):
        # Inicialize o Pygame
        pygame.init()

        # Definir dimensões da janela do jogo
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 300

        # Definir cores
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Crie a janela do jogo
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption('Pong')

        # Defina a bola
        self.ball = pygame.Rect(self.WINDOW_WIDTH/2 - 10, self.WINDOW_HEIGHT/2 - 10, 20, 20)

        # Defina as raquetes
        self.paddle1 = pygame.Rect(50, self.WINDOW_HEIGHT/2 - 50, 10, 100)
        self.paddle2 = pygame.Rect(self.WINDOW_WIDTH - 60, self.WINDOW_HEIGHT/2 - 50, 10, 100)

        # Defina a velocidade da bola
        self.ball_speed_x = 1
        self.ball_speed_y = 1

    def run(self):
        # Loop principal do jogo
        while True:
            # Verifique os eventos do Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Movimente as raquetes com as teclas 'W' e 'S'
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddle1.y -= 1
            if keys[pygame.K_s]:
                self.paddle1.y += 1
            if keys[pygame.K_UP]:
                self.paddle2.y -= 1
            if keys[pygame.K_DOWN]:
                self.paddle2.y += 1

            # Movimente a bola
            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            # Faça a bola quicar nas bordas
            if self.ball.y > self.WINDOW_HEIGHT - 20 or self.ball.y < 0:
                self.ball_speed_y *= -1
            if self.ball.x > self.WINDOW_WIDTH - 20 or self.ball.x < 0:
                self.ball_speed_x *= -1

            # Faça a bola quicar nas raquetes
            if self.ball.colliderect(self.paddle1) or self.ball.colliderect(self.paddle2):
                self.ball_speed_x *= -1

           # Obter o estado atual do jogo
            state = [self.ball.x, self.ball.y, self.paddle1.y, self.paddle2.y]

            # Executar o modelo para obter a ação a ser tomada
            action_probs = model.predict([state])[0]
            action = np.argmax(action_probs)

            # Tomar a ação escolhida pela IA
            if action == 1:
                self.paddle2.y -= 5
            elif action == 2:
                self.paddle2.y += 5

            # Limitar o movimento das raquetes
            if self.paddle1.y < 0:
                self.paddle1.y = 0
            elif self.paddle1.y > self.WINDOW_HEIGHT - self.paddle1.height:
                self.paddle1.y = self.WINDOW_HEIGHT - self.paddle1.height

            if self.paddle2.y < 0:
                self.paddle2.y = 0
            elif self.paddle2.y > self.WINDOW_HEIGHT - self.paddle2.height:
                self.paddle2.y = self.WINDOW_HEIGHT - self.paddle2.height

            # Movimentar a bola
            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            # Desenhar o fundo da tela e os objetos do jogo
            self.screen.fill(self.BLACK)
            pygame.draw.rect(self.screen, self.WHITE, self.paddle1)
            pygame.draw.rect(self.screen, self.WHITE, self.paddle2)
            pygame.draw.ellipse(self.screen, self.WHITE, self.ball)

            # Atualize a tela do jogo
            pygame.display.update()

            # Obter o estado atual do jogo
            state = [self.ball.x, self.ball.y, self.paddle1.y, self.paddle2.y]

            # Definir o modelo da rede neural
            model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, input_shape=(4,), activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(3, activation='softmax')
            ])

            # Obter o estado atual do jogo
            state = [self.ball.x, self.ball.y, self.paddle1.y, self.paddle2.y]

            # Executar o modelo para obter a ação a ser tomada
            action_probs = model.predict([state])[0]
            action = np.argmax(action_probs)

            # Tomar a ação escolhida pela IA
            if action == 1:
                self.paddle2.y -= 5
            elif action == 2:
                self.paddle2.y += 5

            # Limitar o movimento da raquete do computador
            if self.paddle2.top < 0:
                self.paddle2.top = 0
            if self.paddle2.bottom > self.WINDOW_HEIGHT:
                self.paddle2.bottom = self.WINDOW_HEIGHT

            # Verificar se a bola saiu do campo
            if self.ball.left < 0 or self.ball.right > self.WINDOW_WIDTH:
            # Reiniciar a bola no centro
                self.ball.center = (self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/2)
            # Reiniciar a velocidade da bola
                self.ball_speed_x *= -1
                self.ball_speed_y *= -1
            else:
            # Verificar se a bola colidiu com alguma raquete
                if self.ball.colliderect(self.paddle1) or self.ball.        colliderect(self.paddle2):
            # Inverter a direção da bola
                    self.ball_speed_x *= -1

            # Mover a bola
            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            # Desenhar o fundo da tela e os objetos do jogo
            self.screen.fill(self.BLACK)
            pygame.draw.rect(self.screen, self.WHITE, self.paddle1)
            pygame.draw.rect(self.screen, self.WHITE, self.paddle2)
            pygame.draw.ellipse(self.screen, self.WHITE, self.ball)

            # Atualizar a tela do jogo
            pygame.display.update()
            