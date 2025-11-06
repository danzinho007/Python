print("Write a program that reads a number from 0 to 9999 and displays each of the separate digits on the screen.")

print("Escreva um programa que leia um número de 0 a 9999 e exiba cada um dos dígitos separadamente na tela.")

# Relembrando :
# Unidade = 1
# Dezena  = 10
# Centena = 100
# Milhar  = 1000
# Dezena de milhar  = 10000
# Centeza de milhar = 10000 
# Milhões =
# Dezena de milhões
# Centena de milhões
# Bilhões
# Dezena de bilhões
# Centena de bilhões 

number=float(input("Digite um número : "))
print(f"O número da posição da unidade é : {number/10}")
print(f"O número da posição da dezena é : {number/100}")
print(f"O número da posição da centeza é : {number/1000}")

