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
