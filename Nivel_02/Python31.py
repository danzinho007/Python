# Executar com F5

#20- O mesmo professor quer sortear a ordem de apresentação de trabalha dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada

import random
a1 = str(input('Primeiro aluno : ')) 
a2 = str(input('Segundo aluno : '))
a3 = str(input('Terceiro aluno : '))
a4 = str(input('Quarto aluno : '))
a5 = str(input('Quinto aluno : '))
lista = [a1, a2, a3, a4, a5]
random.shuffle(lista)
print('A ordem de apresentação será : ')
print(lista)

# ou

from random import shuffle
a1 = str(input('Primeiro aluno: ')) 
a2 = str(input('Segundo aluno : '))
a3 = str(input('Terceiro aluno : '))
a4 = str(input('Quarto aluno : '))
a5 = str(input('Quinto aluno : '))
lista = [a1, a2, a3, a4, a5]
shuffle(lista)
print('A ordem de apresentação será : ', lista)
