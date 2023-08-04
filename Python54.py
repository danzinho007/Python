# 54

# print("Olá" + 1+2+3)
# Resultado : TypeError

# O erro ocorre porque você está tentando concatenar uma string ("Olá") com números inteiros (1, 2 e 3) sem realizar a conversão dos números para strings. Em Python, a concatenação de strings só é possível entre strings, e não com outros tipos de dados.

print("Olá"+"1+2+3")
# Resultado : Olá1+2+3

print("Olá" + str("1+2+3"))
# Resultado : Olá1+2+3

print("Olá" + str(1) + str(2) + str(3))

print("Olá" + "+" + str(1+2+3))

print(f"Olá+{1+2+3}")

print("Olá " + str(1+2+3))

print("Olá" + str(1+2+3))

print("Olá" + 1)
