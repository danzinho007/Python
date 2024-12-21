print("\nWrite a Python program that opens and plays audio from an MP3 file.")
import pygame

pygame.init()
pygame.mixer.music.load('ex031.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():  # Verifica se a música ainda está tocando
    pygame.time.Clock().tick(10)  # Aguarda um pouco para evitar uso excessivo de CPU

pygame.event.wait()
pygame.quit()
