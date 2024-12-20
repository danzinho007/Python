 
import math

print("\nBiblioteca math : ")

print("\nCalcular Logaritmo : ")
# Relembrando : 
# Log 16 na base 2 ?
# Qual número que eleve a base 2 seja igual a 16 ? 
# Resposta 4, pois 2 elevado a 4  é 16
# Log 36 na base 6 = 2 pois 6² = 36
# Qual número que eleve a base 6 seja igual a 36 ? 
# Resposta  2, pois 6² é 36
# Base 𝑒 (𝑒≈2.718e≈2.718) 
# E usada em matemática avançada, principalmente em cálculos de crescimento exponencial e análise de dados.

number = float(input("\nDigite um número "))
base = float(input("Digite a base : "))
print(f"O logaritmo de {number} na base {base} é {math.log(number,base):.2f}")
print(f"O logaritmo base 10 de {number} é {math.log10(number):.2f}")
print(f"O logaritmo natural (base e) de {number} é {math.log(number):.2f}")


print(f"O valor de π é {math.pi}")
print(f"O valor de e é {math.e}")
print(f"A constante tau (2π) é {math.tau}")

numero = float(input("Digite um número: "))
print(f"A raiz quadrada de {numero} é {math.sqrt(numero):.2f}")
expoente = int(input("Digite um expoente: "))
print(f"{numero} elevado a {expoente} é {math.pow(numero, expoente):.2f}")

numero = float(input("Digite um número decimal: "))
print(f"Arredondado para baixo: {math.floor(numero)}")
print(f"Arredondado para cima: {math.ceil(numero)}")
print(f"Truncado (parte inteira): {math.trunc(numero)}")

numero = int(input("Digite um número inteiro não negativo: "))
print(f"O fatorial de {numero} é {math.factorial(numero)}")

cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))
hipotenusa = math.hypot(cateto1, cateto2)
print(f"A hipotenusa é {hipotenusa:.2f}")

valor = float(input("Digite um valor entre -1 e 1 para calcular arcos: "))
print(f"O arco seno de {valor} é {math.degrees(math.asin(valor)):.2f}°")
print(f"O arco cosseno de {valor} é {math.degrees(math.acos(valor)):.2f}°")
print(f"O arco tangente de {valor} é {math.degrees(math.atan(valor)):.2f}°")

base = float(input("Digite a base do logaritmo: "))
numero = float(input("Digite o número: "))
print(f"O logaritmo de {numero} na base {base} é {math.log(numero, base):.2f}")
print(f"O número {numero} elevado à {base} é {math.pow(numero, base):.2f}")

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))
angulo = math.degrees(math.atan2(y, x))
print(f"O ângulo da coordenada ({x}, {y}) em relação à origem é {angulo:.2f}°")

angulo_graus = float(input("Digite o ângulo em graus: "))
print(f"{angulo_graus}° é igual a {math.radians(angulo_graus):.2f} radianos")
angulo_radianos = float(input("Digite o ângulo em radianos: "))
print(f"{angulo_radianos} radianos é igual a {math.degrees(angulo_radianos):.2f} graus")

numero = float(input("Digite um número: "))
print(f"O seno hiperbólico de {numero} é {math.sinh(numero):.2f}")
print(f"O cosseno hiperbólico de {numero} é {math.cosh(numero):.2f}")
print(f"A tangente hiperbólica de {numero} é {math.tanh(numero):.2f}")