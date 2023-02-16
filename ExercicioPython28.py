# Executar com F5

# Comentário

#18- Faça um programa que leia um ângulo e mostre na tela o valor do :
#Seno, Cosseno, Tangente, Secante, Cossecante e Cotangente

# Importando só o que vai usar :

from math import radians, sin, cos, tan

angulo = float(input('Informe o ângulo : '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
secante = 1 / cosseno
cossecante = 1 / seno
cotangente = 1 / tangente
cotangente1 = 1 / tan(radians(angulo))
print('O valor do Seno é {:.2f}, \n Cosseno é {:.2f}, \n Tangente é {:.2f}, \n Secante é {:.2F}, \n Cossecante é {:.2F} e \n Cotangente é {:.2F}' .format(seno, cosseno, tangente, secante, cossecante, cotangente))
print('A tangente vale : {:.2f}' .format(cotangente1))
print(' ')

# Jeito certo :

import math

ang = float(input('Informe o ângulo : '))
n11 = math.sin(math.radians(ang))
n22 = math.cos(math.radians(ang))
n33 = math.tan(math.radians(ang))
n44 = 1 / n22
n55 = 1 / n11
n66 = 1 / n33
n77 = 1 / math.tan(math.radians(ang))
print('O valor do Seno é {:.2f}, \n Cosseno é {:.2f}, \n Tangente é {:.2f}, \n Secante é {:.2F}, \n Cossecante é {:.2F} e \n Cotangente é {:.2F}' .format(n11, n22, n33, n44, n55, n66))
print('A tangente vale : {:.2f}' .format(n77))
print(' ')

#Convertendo de Grau pra Radiano

graus = 45
radianos = graus * (math.pi / 180)
seno = math.sin(radianos)
print(seno)
print(' ')

# Fazendo direto :

n1 = float(input('Informe o ângulo : '))
n1 = math.sin(n1)
# n1 ta armazenando o ângulo informado
print('O valor do Seno é {:.2f}' .format(n1))
 
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
