#Desafios

#17- Faça um programa que leia o comprimento do Cateto Oposto e do Cateto Adjacente de um Triângulo Retângulo, calcule e mostre o comprimento da hipotenusa

n1 = float(input('Diga o Cateto Oposto : '))
n2 = float(input('Diga o Cateto Adjacente : '))
hip = (n1 ** 2) + (n2 ** 2)
print('A hipotenusa vale {}' .format(hip))

#18- Faça um programa que leia um ângulo e mostre na tela o valor do :
#Seno, Cosseno, Tangente, Secante, Cossecante e Cotangente

import math
n1 = float(input('Informe o ângulo : '))
n1 = math.sin(n1)
print('O valor de Seno é {:.2f}' .format(n1))

#19- Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido

#20- O mesmo professor quer sortear a ordem de apresentação de trabalha dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada

#21- Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
