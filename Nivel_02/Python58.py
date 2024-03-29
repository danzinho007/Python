# 22
# Crie um programa que leia o nome completo de uma pessoa e mostre :
# O nome com todas as letras Maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo ( sem considerar espaços )
# Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome complet: ")).strip()
print("Analisando seu nome ...")
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(' ')))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))
separa = nome.split()
print(separa)
print("Seu primeiro é {} e ele tem {} letras".format(separa[0], len(separa[0])))
