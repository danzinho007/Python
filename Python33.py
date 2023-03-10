# Executar com F5

import math
num = int(input('Digite um número : '))

from math import acos
# Pra funcionar o número precisa estar entre -1 e 1
coss = math.acos(num)
print('O acos de {} é igual a {}' .format(num, coss))

from math import acosh
v1 = math.acosh(num)
print('O acos de {} é igual a {}' .format(num, v1))

from math import asin
v2 = math.asin(num)
print('O acos de {} é igual a {}' .format(num, v2))

from math import asinh
v3 = math.asinh(num)
print('O acos de {} é igual a {}' .format(num, v3))

from math import atan
v4 = math.atan(num)
print('O atan de {} é igual a {}' .format(num, v4))

# from math import atan2
# A função atan2() calcula a tangente inversa de dois números passados como argumentos, sendo o primeiro argumento a coordenada y e o segundo argumento a coordenada x de um ponto em um plano cartesiano. A mensagem de erro indica que a função foi chamada com apenas um argumento, então você precisa fornecer dois argumentos para a função atan2().
# v5 = math.atan2(num)
# print('O acos de {} é igual a {}' .format(num, v5))

# Ver Python34.py
# from math import atanh
# # Pra funcionar o número precisa estar entre -1 e 1
# # Precisa ser um número flutuante
# v6 = math.atanh(num)
# print('O atanh de {} é igual a {}' .format(num, v6))

from math import cbrt
v7 = math.cbrt(num)
print('O acos de {} é igual a {}' .format(num, v7))

from math import ceil
v8 = math.ceil(num)
print('O acos de {} é igual a {}' .format(num, v8))

# Ver Python34.py
# from math import comb
# A função comb() é usada para calcular o número de combinações de n objetos tomados r de cada vez. Para corrigir o erro, você precisa passar dois argumentos para a função comb(): o primeiro argumento é o número total de objetos e o segundo argumento é o número de objetos escolhidos em cada combinação.
# v9 = math.comb(num)
# print('O acos de {} é igual a {}' .format(num, v9))

# Ver Python34.py
# from math import copysign
# #  a função math.copysign(), que espera dois argumentos. A função copysign() é usada para retornar um número com o valor absoluto de um argumento (num) e o sinal do outro argumento (sign).
# v10 = math.copysign(num)
# print('O acos de {} é igual a {}' .format(num, v10))
