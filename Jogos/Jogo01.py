# Video
# https://www.youtube.com/watch?v=0grkxfpiK0w

import pygame

width = 1200
height = 800

class_Player(pygame.sprite.Sprite):
       def_init_(self):
              pygame.sprite.Sprite...init(self)

pygame.init()
game_window = pygame.display.set_mode(width, height)
pygame.display.set.caption("Título")

gameloop = True
def draw():
      game.window.fill(255, 255, 0)

while gameloop:
         for event in pygame.event.get():
               if event.type == pygame.QUIT:
	  pygame.quit()
	  break
         pygame.display.update()