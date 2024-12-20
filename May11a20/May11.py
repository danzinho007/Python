print("\nWrite a program that reads the width and height of a wall in meters, calculates the amount of paint needed to paint it, knowing that each liter of paint paints an area of 2m².")

# Calculando
# Parede com 2x2 terá 4 quadrados ou 4m²
# Se 1 pintura pinta 2m², logo serão necessário :
# 1l = 2m²
# x  = 4m² > x = 4/2 > x = 2l
# Logo serão necessários 2l de tinta
# Logo Largura * Altura / 2

print("Digite os valores na forma inteira (2) ou decimal (2.0)")
width = float(input("\nQuanto de largura a parede tem ? "))
height = float(input("Quanto de altura a parede tem ? "))
print(f"Para pintar uma parede de {width} com {height} serão necessários ")
print(f"{width * height / 2:.2f}l de tinta")
