# Comentário

#18- Faça um programa que leia um ângulo e mostre na tela o valor do :
#Seno, Cosseno, Tangente, Secante, Cossecante e Cotangente

import math

#Convertendo de Grau pra Radiano

graus = 45
radianos = graus * (math.pi / 180)
seno = math.sin(radianos)
print(seno)

#ou Convertendo com comando

n1 = float(input('Informe o ângulo : '))
n1 = math.sin(n1)
# n1 ta armazenando o ângulo informado
print('O valor de Seno é {:.2f}' .format(n1))

n2 = math.cos(n1)
#Retorna o cosseno de x radianos.
print('O valor do Cosseno em radianos é {}' .format(n2))

n3 = math.tan(n1)
#Retorna o tangente de x radianos.
print('O valor da tangente em radianos é {:.2f}' .format(n3))

n4 = 1 / n2
print('O valor da Secante é de {:.2f}' .format(n4))

n5 = 1 / n1
print('O valor da Cossecante é {:.2}' .format(n5))

n6 = 1 / n3
print('O valor da Cotangente é de {:.2f}' .format(n6))

#19- Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido

#20- O mesmo professor quer sortear a ordem de apresentação de trabalha dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada

#21- Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
