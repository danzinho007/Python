import math
num = int(input('Digite um númer : '))
raiz = math.sqrt(num)
# Aqui encima ele está fazendo RaizQuadradrada da Biblioteca math do Número que foi digitado antes e guardando o resultado na variável raiz
#ou seja
# Ele irá guardar na variável raiz algo que veio da Biblioteca math que é RaizQuadrada do número que foi digitado antes

print('A raiz de {} é igual a {}' .format(num, raiz))
print('A raiz de {} é igual a {:.2f}' .format(num, raiz))
#ou
print('A raiz de {} é igual a {}' .format(num, math.floor(raiz)))
print('A raiz de {} é igual a {}' .format(num, math.ceil(raiz)))

num1 = int(input('Digite um númer : '))
raiz1 = math.sqrt(num1)
print('A raiz de {} é igual a {}' .format(num1, raiz1))

from math import floor
num2 = int(input('Digite um númer : '))
raiz2 = math.sqrt(num2)
print('A raiz de {} é igual a {}' .format(num2, floor(raiz)))

import random
num3 = random.random()
print(num3)

import random
num4 = random.randint(1, 10)
print(num4)


# print(emoji.emojize("Olá, Mundo :sunglasses:", use_aliases=True))

# Operações que tem em math : Testar todas !!!
#Digitando from math import e depois CTRL + Espaço, a pessoa pode ver todas operações que tem em math

