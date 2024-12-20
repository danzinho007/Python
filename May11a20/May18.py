print("# Write a program that reads any angle and displays on the screen the value of the sine, cosine and tangent of that angle.")

print("# Escreva um programa que leia qualquer ângulo e exiba na tela o valor do seno, cosseno e tangente desse ângulo.")

# Relembrando :
# Seno = cateto oposto sobre hipotenusa
# Cosseno = cateto adjacente sobre hipotenusa
# Tangente = cateto oposto sobre cateto adjacente
# Secante = 1 / cosseno
# Cossecante = 1 / seno
# Cotangente = 1 / tangente

import math

angulo=float(input("Informe o ângulo : "))
#Convertendo o ângulo para radianos e depois calculando o seno :
print(f"O seno vale {math.sin(math.radians(angulo)):.1f}")
print(f"O cosseno vale {math.cos(math.radians(angulo)):.1f}")
print(f"A tangente vale {math.tan(math.radians(angulo)):.1f}")
print(f"A secante vale {(1/math.sin(math.radians(angulo))):.1f}")
print(f"A cossecante vale {1/math.cos(math.radians(angulo)):.1f}")
print(f"A cotangente vale {1/math.tan(math.radians(angulo)):.1f}")
