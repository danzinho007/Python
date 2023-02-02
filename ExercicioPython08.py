#!!! Desafios : 

#010 : Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considera U$$1.00 = R$ 3.27

print('Saiba aqui quantos dólares você tem ? R$')
print('Pode por os centavos também')
nDin = float(input('Digite aqui quantos reais possui : '))
dolar = ( nDin * 1.00 ) / 3.27
# ou
dolar1 = nDin / 3.27

input('Tendo em consideração 1 dólar = 3.27, você tem {:.2f} U$$' .format(dolar))
input('Tendo em consideração 1 dólar = 3.27, você tem {:.2f} U$$' .format(dolar1))
print(' ')

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

#012 : Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

# 10 % de 1.500 é > 1.500 * 10 / 100 > 150.0
# 15 % de   875 é >   875 * 15 / 100 > 131.25

print("Saibe aqui o preço de qualquer produto com seu desconto")

produto = float(input('Qual é o preço do produto ? R$ '))
desconto =float(input('Agora digite quantos % será o desconto : '))

precodesc = ( produto * desconto ) / 100
preconovo = produto - precodesc

#ou

preconovo1 = produto - ( produto * desconto / 100 )

input('Seu produto de {} com desconto de {}, passara a ser {}' .format(produto, desconto, preconovo))

input('Seu produto de {} com desconto de {}, passara a ser {}' .format(produto, desconto, preconovo1))

print(' ')

#013 : Faça um algoritmo que leia o salário de um funcionário e mostra seu novo salário com 15% de aumento

#Salário - Porcentagem
#100     -  100%
#  x     -   10%
# 10 * 100 / 100
# 1000 / 100
# 10
# 10% de 100 é 10, logo 100 + 110 = Novo Salário

print("Saiba aqui qual será o valor de qualquer produto com o aumento")

valor = float(input('Digite aqui o valor do produto : R$ '))
desc = float(input('Digite aqui o valor do aumento : % '))

descvalor = ( valor * desc ) / 100
novovalor = valor + descvalor

#ou

novovalor1 = valor ( valor * desc ) / 100

input('Seu salário de R$ {} com {}% será de {}' .format(valor, desc, novovalor))
input('Seu salário de R$ {:.2f} com {}% será de {:.2f}' .format(valor, desc, novovalor1))
