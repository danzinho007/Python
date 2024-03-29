# Executar com F5

#011 : Faça um programa que leia a largura e a altura de uma parede em m, calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

#Calculando áreas :
#Círculo : π ( Pi é igual a 3.14 ) * r * r
#Quadrado : L * L 
#Losango : D * d / 2
#Retãngulo : b * h
#Trapézio : ( B + b ) * h / 2
#Triângulo : A = b * h / 2

print("Saibe aqui a área de qualquer Parede e quanto irá gastar de tinta. Sabendo 1l = 2m²")

#Litro - m²
# 1    - 2
# x     - area

largura = float(input('Digite o valor da largura em m : '))
altura = float(input('Digite o valor da altura em m : '))
area = largura * altura
litro = ( area * 1 ) / 2
#ou
litro1 = area / 2

input('Tendo em consideração que a Parede é de {} m², logo você irá gastar {} litros de tinta' .format(area, litro))
input('Tendo em consideração que a Parede é de {} m², logo você irá gastar {} litros de tinta' .format(area, litro1))

print(' ')