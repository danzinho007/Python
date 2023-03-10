# Testando fmod(x, y)
import math

num1 = float(input('Digite o dividendo: '))
num2 = float(input('Digite o divisor: '))

v24 = math.fmod(num1, num2)

print('O resto da divisão entre {} e {} é igual a {}'.format(num1, num2, v24))

# 

import math

num1 = float(input('Digite o dividendo: '))
num2 = float(input('Digite o divisor: '))

q, r = divmod(num1, num2)

print('A divisão de {} por {} resulta em {} com resto igual a {}'.format(num1, num2, q, r))


# -------------------------------------------

# Testando fsum(x,y,)
import math

num = [1, 2, 3, 4, 5]
v26 = math.fsum(num)
print(v26)

# 

# Testando inf
import math

v30 = math.inf  # infinito positivo
print(v30)  # saída: inf

v31 = -math.inf  # infinito negativo
print(v31)  # saída: -inf
