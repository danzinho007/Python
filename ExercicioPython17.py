# Executar com F5

#Desafios

#17- Faça um programa que leia o comprimento do Cateto Oposto e do Cateto Adjacente de um Triângulo Retângulo, calcule e mostre o comprimento da hipotenusa

# Hipotenusa é a Raiz Quadrada da Soma dos Catetos ( Oposto e Adjacente ) ao Quadrado 
# ou >>> Quadrado da Hipotenusa é igual a Soma do Quadrado dos Catetos
#  Ou seja >>> Hip = Raiz Quadrada ( Co² + Ca² )

co = float(input('Diga o Cateto Oposto : '))
ca = float(input('Diga o Cateto Adjacente : '))
hip = (co ** 2 + ca ** 2) ** ( 1/2 )
print('A hipotenusa vale {:.2f}' .format(hip))

# Ou

from math import hypot
co2 = float(input('Diga o Cateto Oposto : '))
ca2 = float(input('Diga o Cateto Adjacente : '))
hip2 = math.hypot(co2, ca2)
print('A hipotenusa vale {:.2f}' .format(hip2))

# Ou

import math
co1 = float(input('Diga o Cateto Oposto : '))
ca1 = float(input('Diga o Cateto Adjacente : '))
hip1 = math.hypot(co1, ca1)
print('A hipotenusa vale {:.2f}' .format(hip1))
