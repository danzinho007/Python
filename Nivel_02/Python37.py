# Executar com F5

import math
num = int(input('Digite um número : '))

from math import fabs
v21 = math.fabs(num)
print('O acos de {} é igual a {}' .format(num, v21))

from math import factorial
v22 = math.factorial(num)
print('O acos de {} é igual a {}' .format(num, v22))

from math import floor
v23 = math.floor(num)
print('O acos de {} é igual a {}' .format(num, v23))

# from math import fmod
# passando apenas um. O primeiro argumento deve ser o dividendo e o segundo argumento deve ser o divisor. 
# v24 = math.fmod(num)
# print('O acos de {} é igual a {}' .format(num, v24))

from math import frexp
v25 = math.frexp(num)
print('O acos de {} é igual a {}' .format(num, v25))

# from math import fsum
# A função math.fsum() espera um iterável (uma lista, tupla, conjunto, etc.) como argumento, mas você está passando um número inteiro (num). Você precisa converter o número em uma lista, tupla ou conjunto antes de passá-lo para a função math.fsum().
# v26 = math.fsum(num)
# print('O acos de {} é igual a {}' .format(num, v26))

from math import gamma
v27 = math.gamma(num)
print('O acos de {} é igual a {}' .format(num, v27))

from math import gcd
v28 = math.gcd(num)
print('O acos de {} é igual a {}' .format(num, v28))

from math import hypot
v29 = math.hypot(num)
print('O acos de {} é igual a {}' .format(num, v29))

# from math import inf
# A função inf do módulo math em Python retorna um valor float que representa o infinito positivo ou negativo, dependendo do sinal passado como argumento. Não é necessário chamar a função inf em um valor numérico.
# O erro "TypeError: 'float' object is not callable" ocorreu porque você tentou chamar a função inf em um número, o que não é possível.
# v30 = math.inf(num)
# print('O acos de {} é igual a {}' .format(num, v30))
