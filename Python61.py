# 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input("Qual é o seu nome completo ? ")).strip()
print("Seu nome tem Silva ? {}".format(nome[:5] == "Silva")) #só aceita começando com Silva
print("Seu nome tem Silva ? {}".format("Silva" in nome)) #só aceita Silva!!!
print("Seu nome tem Silva ? {}".format("silva" in nome.lower()))#jeito correto
