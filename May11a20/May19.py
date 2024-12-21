print("# A teacher wants to draw one of his four students to erase the board. Make a program that helps him, reading the name of the students and writing the name of the chosen one on the screen.")

print("# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome dos alunos e escrevendo o nome do escolhido na tela.")

import random

# O que vem de um input é uma string !!!
nameOne = input('First students name:')
print(f"{type(nameOne)}")   
print(f"{nameOne} é {type(nameOne)}")   
nameTwo = input('Second students name:')
nameThree = input('Third students name:')
nameFour = input('Fourth students name:')

list = [nameOne, nameTwo, nameThree, nameFour]
chosen = random.choice(list)

print(f'The student chosen to erase the board is {chosen}.')
