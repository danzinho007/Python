#Desafios

#16- Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex : 6.127 >>> O número 6.127 tem a parte inteira 6

import math
print("Digite um número e irei informar a sua parte inteira")
n1 = float(input('Digite um númer : '))

teste1 = math.ceil(n1)
#ceil vai retornar o valor inteiro, caso tenha virgula ele irá somar +1
print('O valor ceil é {}' .format(teste1))

teste2 = math.fabs(n1)
#fabs vai retornar o valor absoluto, ou seja vai deixar positivo o número caso ele seja negativo
print('O valor é {}' .format(teste2))

teste3 = math.frexp(n1)
#frexp vai retornar a mantissa ( parte decimal de um logaritmo ) e o expoente de como par
#Mantissa é a parte decimal de um número, é um número entre 0,5 e 1
# A mantissa é um número entre 0,5 e 1 (inclusive) que representa a parte fracionária do número original, enquanto o expoente é o deslocamento do ponto decimal para a direita ou para a esquerda que é necessário para obter o número original a partir da mantissa.
# Por exemplo, math.frexp(10) retornaria (0.625, 4), indicando que 10 é equivalente a 0.625 * 2^4 > 0.625 * 16 > 10
# Outro exemplo : frexp de 100 é ( 0,78125, 7 ), ou seja 2 elevado a 7
#   2 x 2 = 4 ( 2 )
#       4 x 2 = 8 ( 3 )
#           8 x 2 = 16 ( 4 )
#               16 x 2 = 32 ( 5 )
#                   32 x 2 = 64 ( 6)
#                       64 x 2 = 128 ( 7 )
# 0,78125 * 128 = 100
print('O valor frexp é {}' .format(teste3))
# https://docs.python.org/pt-br/3/library/math.html#number-theoretic-and-representation-functions
# https://www.w3schools.com/python/ref_math_frexp.asp
# https://acervolima.com/python-funcao-frexp/
# https://www.youtube.com/watch?v=PYftCrnrSOg
# https://www.youtube.com/watch?v=QRJUac1ZfWs

# teste4 = math.acos(n1)
# print('O valor é {}' .format(teste4))

teste5 = math.acosh(n1)
#Retorna o cosseno hiperbólico inverso de x.
print('O valor acosh é {}' .format(teste5))

#teste6 = math.asin(n1)
#Retorna o arco seno de x, em radianos. O resultado está entre -pi/2 e pi/2.
# print('O valor é {}' .format(n1))

teste7 = math.asinh(n1)
#Retorna o seno hiperbólico inverso de x.
print('O valor é {}' .format(teste7))

teste8 = math.atan(n1)
#Retorna o arco tangente de x, em radianos. O resultado está entre -pi/2 e pi/2.
print('O valor atan é {}' .format(teste8))

# teste9 = math.atan2(n1)
#Retorna atan(y / x), em radianos. O resultado está entre -pi e pi. O vetor no plano da origem ao ponto (x, y) faz este ângulo com o eixo X positivo. O ponto de atan2() é que os sinais de ambas as entradas são conhecidos por ele, então ele pode calcular o quadrante correto para o ângulo. Por exemplo, atan(1) e atan2(1, 1) são ambos pi/4, mas atan2(-1, -1) é -3*pi/4.
# print('O valor é {}' .format(n1))

#teste10 = math.atanh(n1)
#Retorna a tangente hiperbólica inversa de x.
# print('O valor é {}' .format(n1))

teste11 = math.cbrt(n1)
#Retorna a raiz cúbica de x.
print('O valor cbrt é {}' .format(teste11))

# teste12 = math.comb(n1)
# print('O valor é {}' .format(n1))

# teste13 = math.copysign(n1)
# print('O valor é {}' .format(n1))

teste14 = math.cos(n1)
print('O valor é {}' .format(teste14))

#teste15 = math.ciel(n1)
print('O valor é {}' .format(n1))

#teste16 = math.factorial(n1)
print('O valor é {}' .format(n1))

teste17 = math.floor(n1)
print('O valor é {}' .format(n1))

#teste18 = math.fsum(n1)
print('O valor é {}' .format(n1))

#teste19= math.gcd(n1)
print('O valor é {}' .format(n1))

#teste20 = math.infinite(n1)
print('O valor é {}' .format(n1))

teste21 = math.isinf(n1)
print('O valor é {}' .format(n1))

#teste22 = math.isqnan(n1)
print('O valor é {}' .format(n1))

#teste23 = math.isqrt(n1)
print('O valor é {}' .format(n1))

teste24 = math.modf(n1)
print('O valor é {}' .format(n1))

teste25 = math.trunc(n1)
print('O valor é {}' .format(n1))

teste26 = math.ulp(n1)
print('O valor é {}' .format(n1))

teste27 = math.cbrt(n1)
print('O valor é {}' .format(n1))

teste28 = math.exp(n1)
print('O valor é {}' .format(n1))

teste29 = math.exp2(n1)
print('O valor é {}' .format(n1))

teste30 = math.expm1(n1)
print('O valor é {}' .format(n1))

teste31 = math.log1p(n1)
print('O valor é {}' .format(n1))

teste32 = math.log2(n1)
print('O valor é {}' .format(n1))

teste33 = math.log10(n1)
print('O valor é {}' .format(n1))

teste34 = math.sqrt(n1)
print('O valor é {}' .format(n1))

#teste35 = math.acos(n1)
print('O valor é {}' .format(n1))

#teste36 = math.asin(n1)
print('O valor é {}' .format(n1))

teste37 = math.atan(n1)
print('O valor é {}' .format(n1))

teste38 = math.cos(n1)
print('O valor é {}' .format(n1))

teste39 = math.sin(n1)
print('O valor é {}' .format(n1))

teste40 = math.tan(n1)
print('O valor é {}' .format(n1))

teste41 = math.degrees(n1)
print('O valor é {}' .format(n1))

teste42 = math.radians(n1)
print('O valor é {}' .format(n1))

teste43 = math.acosh(n1)
print('O valor é {}' .format(n1))

teste44 = math.asinh(n1)
print('O valor é {}' .format(n1))

#teste45 = math.atanh(n1)
print('O valor é {}' .format(n1))

teste46 = math.cosh(n1)
print('O valor é {}' .format(n1))

teste47 = math.sinh(n1)
print('O valor é {}' .format(n1))

teste48 = math.tanh(n1)
print('O valor é {}' .format(n1))

teste49 = math.erf(n1)
print('O valor é {}' .format(n1))

teste50 = math.erfc(n1)
print('O valor é {}' .format(n1))

teste51 = math.gamma(n1)
print('O valor é {}' .format(n1))

teste52 = math.lgamma(n1)
print('O valor é {}' .format(n1))

#17- Faça um programa que leia o comprimento do Cateto Oposto e do Cateto Adjacente de um Triângulo Retângulo, calcule e mostre o comprimento da hipotenusa

#18- Faça um programa que leia um ângulo e mostre na tela o valor do :
#Seno, Cosseno, Tangente, Secante, Cossecante e Cotangente

#19- Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido

#20- O mesmo professor quer sortear a ordem de apresentação de trabalha dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada

#21- Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
