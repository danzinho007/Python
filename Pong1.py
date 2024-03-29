import numpy as np
import pygame
import sys
import tensorflow as tf

class PongGame:
    def __init__(self):
        self.window_width = 400
        self.window_height = 300
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        pygame.init()

        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Pong')

        self.ball = pygame.Rect(self.window_width/2 - 10, self.window_height/2 - 10, 20, 20)
        self.paddle1 = pygame.Rect(50, self.window_height/2 - 50, 10, 100)
        self.paddle2 = pygame.Rect(self.window_width - 60, self.window_height/2 - 50, 10, 100)
        self.ball_speed_x = 1
        self.ball_speed_y = 1

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddle1.y -= 1
            if keys[pygame.K_s]:
                self.paddle1.y += 1
            if keys[pygame.K_UP]:
                self.paddle2.y -= 1
            if keys[pygame.K_DOWN]:
                self.paddle2.y += 1

            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            if self.ball.y > self.window_height - 20 or self.ball.y < 0:
                self.ball_speed_y *= -1
            if self.ball.x > self.window_width - 20 or self.ball.x < 0:
                self.ball_speed_x *= -1

            if self.ball.colliderect(self.paddle1) or self.ball.colliderect(self.paddle2):
                self.ball_speed_x *= -1

            self.screen.fill(self.black)
            pygame.draw.rect(self.screen, self.white, self.paddle1)
            pygame.draw.rect(self.screen, self.white, self.paddle2)
            pygame.draw.ellipse(self.screen, self.white, self.ball)

            pygame.display.update()

if __name__ == '__main__':
    # Definir o modelo da rede neural
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, input_shape=(4,), activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax')
    ])

    # Crie um objeto PongGame
    pong_game = PongGame()

    # Inicie o jogo
    pong_game.run()
