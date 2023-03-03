# Executar com F5

#19- Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido

import math
n1 = input('Digite aqui o nome do 1° aluno : ')
n2 = input('Digite aqui o nome do 2°       : ')
n3 = input('Digite aqui o nome do 3°       : ')
n4 = input('Digite aqui o nome do 4°       : ')
n5 = input('Digite aqui o nome do 5°       : ')

import random
sorteio = random.randint(1, 5)
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
print('A pessoa sorteada é : {}' .format(sorteio))

# ou

import random
# ou from random import choice, remover random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = str(input('Quinto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}' .format(escolhido))

# ou

from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = str(input('Quinto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}' .format(escolhido))
