#19- Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido

import math
n1 = input('Digite aqui o nome do 1° aluno : ')
n2 = input('Digite aqui o nome do 2°       : ')
n3 = input('Digite aqui o nome do 3°       : ')
n4 = input('Digite aqui o nome do 4°       : ')
n5 = input('Digite aqui o nome do 5°       : ')
import random
sorteio = random.randint(n1, n5)
print('A pessoa sorteada é : {}' .format(sorteio))

# ou

