#Desafios

#17- Faça um programa que leia o comprimento do Cateto Oposto e do Cateto Adjacente de um Triângulo Retângulo, calcule e mostre o comprimento da hipotenusa

n1 = float(input('Diga o Cateto Oposto : '))
n2 = float(input('Diga o Cateto Adjacente : '))
hip = (n1 ** 2) + (n2 ** 2)
print('A hipotenusa vale {}' .format(hip))
