# Testando atan2(x,y)

import math

x = 3
y = 4

result = math.atan2(y, x)

print("O ângulo em radianos é:", result)

# Só não pode digitar -1 ou 1
import math

num = float(input('Digite um número: '))

if num < -1 or num > 1:
    print('O número precisa estar no intervalo -1 a 1')
else:
    v6 = math.atanh(num)
    print('O atanh de {} é igual a {:.2f}'.format(num, v6))

# Testando math.comb
import math

n = int(input("Digite o número total de objetos: "))
r = int(input("Digite o número de objetos escolhidos em cada combinação: "))

comb = math.comb(n, r)

print("O número de combinações é:", comb)

# Testando math.copysign
import math

num = float(input("Digite um número: "))
sign = float(input("Digite um número cujo sinal você deseja usar: "))

result = math.copysign(num, sign)

print("O resultado é:", result)

