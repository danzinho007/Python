#28- Write a program that makes the computer "think" of an integer between 0 and 5 and ask the user to try find out which number was chosen by the computer. The program should write on the screen whether the user won or it lost.

#28- Escreva um programa que faça o computador "pensar" em um inteiro entre 0 e 5 e peça ao usuário para tentar descobrir qual número foi escolhido pelo computador. O programa deve escrever na tela se o usuário ganhou ou perdeu.

import random  # Biblioteca para gerar números aleatórios

# Computador escolhe um número aleatório entre 0 e 5
numeroComputador = random.randint(0, 5)

# Usuário tenta adivinhar
print("O computador pensou em um número entre 0 e 5...")
numeroUsuario = int(input("Tente adivinhar o número: "))

if numeroUsuario == numeroComputador:
    print(f"Parabéns! Você acertou, o número era {numeroComputador}.")
else:
    print(f"Que pena! Você errou. O número era {numeroComputador}.")
