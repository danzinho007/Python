# 23
# Faça um programa que leia um número de 0 a 9.999 e mostre na tela cada um dos dígitos separados 
# Ex Digite um nùmero : 1.834
# unidade : 4
# dezena : 3
# centena : 8
# milhar : 1
# Fazer com String e Matematicamente !!!

# Forma String 

num = int(input("Informe um número: "))
n = str(num)
print("Analisando o número {}".format(num))
print("Unidade: {}".format(n[3]))
print("Dezena: {}".format(n[2]))
print("Centena: {}".format(n[1]))
print("Milhar: {}".format(n[0]))

# Forma Numérica

num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analisando o número {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centeza: {}".format(c))
print("Milhar: {}".format(m))
