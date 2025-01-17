# 27 
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex : Ana Maria de Souza
# primeiro : Ana
# último : Souza

n = str(input("Digite seu nome completo: ")).strip()
name = n.split()
print("Muito prazer em te conhecer {}".format(n))
print("Seu primeiro nome é {}".format(name[0]))
print("Seu último nome é {}".format(name[len(name)-1]))
