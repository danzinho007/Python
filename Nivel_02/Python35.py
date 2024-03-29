# Executar com F5

import math
num = int(input('Digite um número : '))

from math import acos
# Pra funcionar o número precisa estar entre -1 e 1
coss = math.acos(num)
print('O acos de {} é igual a {}' .format(num, coss))

from math import cos
v11 = math.cos(num)
print('O acos de {} é igual a {}' .format(num, v11))

from math import cosh
v12 = math.cosh(num)
print('O acos de {} é igual a {}' .format(num, v12))

from math import degrees
v13 = math.degrees(num)
print('O acos de {} é igual a {}' .format(num, v13))

# from math import dist
# A função math.dist() espera dois argumentos, cada um representando um ponto no espaço. Você está passando apenas um argumento, que é um número inteiro. Por isso ocorre a exceção de tipo. Para corrigir isso, você precisa passar dois pontos ao invés de um número inteiro
# v14 = math.dist(num)
# print('O acos de {} é igual a {}' .format(num, v14))

# from math import e
# A exceção "TypeError: 'float' object is not callable" ocorre quando você tenta chamar um número como se fosse uma função. Isso pode acontecer quando você usa parênteses em torno de um número sem uma função correspondente. 
# v15 = math.e(num)
# print('O acos de {} é igual a {}' .format(num, v15))

from math import erf
v16 = math.erf(num)
print('O acos de {} é igual a {}' .format(num, v16))

from math import erfc
v17 = math.erfc(num)
print('O acos de {} é igual a {}' .format(num, v17))

from math import exp
v18 = math.exp(num)
print('O acos de {} é igual a {}' .format(num, v18))

from math import exp2
v19 = math.exp2(num)
print('O acos de {} é igual a {}' .format(num, v19))

from math import expm1
v20 = math.expm1(num)
print('O acos de {} é igual a {}' .format(num, v20))
