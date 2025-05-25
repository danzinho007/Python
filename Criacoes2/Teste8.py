dividendo = input("Digite o dividendo: ") # Digitei 215
divisor = int(input("Digite o divisor: ")) # Digitei 5

indice = 0
num = int(dividendo[indice]) # num = 2

print(f"{dividendo} | {divisor}") # 215 | 5

resultado = ""

"""
Primeira iteração:

num = 2 (primeiro algarismo de 215)
num não pode ser dividido por 5, então o próximo algarismo é anexado, formando 21.
quociente = 4 e resto = 1.

Segunda iteração:
num = 15 (resto 1 + próximo algarismo 5).
quociente = 3 e resto = 0.

Terceira iteração:
# Não há mais algarismos, então a divisão termina.
"""

while indice < len(dividendo):
    if num < divisor and indice+1 < len(dividendo):
        indice += 1
        num = num * 10 + int(dividendo[indice])

    quociente = num // divisor
    resto = num % divisor

    resultado += str(quociente)

    indice += 1
    if indice < len(dividendo):
        num = resto * 10 + int(dividendo[indice])
    else:
        num = resto

    if len(dividendo) <= 3:
        print(f" {num:<2} | {resultado}")
    else:
       print(f"    {num:<2} | {resultado}") 
       
print(f'O resultado entre {dividendo} e o {divisor} é {resultado}')
