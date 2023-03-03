#!!! Desafios : 

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

