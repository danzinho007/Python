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
print('O valor fabs é {}' .format(teste2))

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

#teste4 = math.acos(n1)
#Retorna o arco cosseno de x, em radianos. O resultado está entre 0 e pi.
#Pra funcionar precisa estar entre -1 e 1
#print('O valor é {}' .format(teste4))

#teste5 = math.acosh(n1)
#Retorna o cosseno hiperbólico inverso de x.
#Pra funcionar precisa >= 1
#print('O valor acosh é {}' .format(teste5))

#teste6 = math.asin(n1)
#Retorna o arco seno de x, em radianos. O resultado está entre -pi/2 e pi/2.
#Pra funcionar precisa estar entre -1 e 1
# print('O valor é {}' .format(n1))

teste7 = math.asinh(n1)
#Retorna o seno hiperbólico inverso de x.
#A função seno hiperbólico inverso (asinh) é uma função matemática que retorna o seno hiperbólico inverso de um número. Ela é definida como a função logarítmica com base no logaritmo natural (ln), de tal forma que: asinh (x) = ln (x + sqrt (x^2 + 1))
print('O valor asinh é {}' .format(teste7))

teste8 = math.atan(n1)
#Retorna o arco tangente de x, em radianos. O resultado está entre -pi/2 e pi/2.
print('O valor atan é {}' .format(teste8))

#teste9 = math.atan2(n1)
#Retorna atan(y / x), em radianos. O resultado está entre -pi e pi. O vetor no plano da origem ao ponto (x, y) faz este ângulo com o eixo X positivo. O ponto de atan2() é que os sinais de ambas as entradas são conhecidos por ele, então ele pode calcular o quadrante correto para o ângulo. Por exemplo, atan(1) e atan2(1, 1) são ambos pi/4, mas atan2(-1, -1) é -3*pi/4.
# 27 = Retorna erro
#print('O valor é {}' .format(teste9))

# teste10 = math.atanh(n1)
#Retorna a tangente hiperbólica inversa de x.
# 27 = Retorna erro
# print('O valor é {}' .format(teste10))

teste11 = math.cbrt(n1)
#Retorna a raiz cúbica de x.
print('O valor cbrt é {}' .format(teste11))

#teste12 = math.comb(n1)
#comb(n, k)
#Retorna o número de maneiras de escolher k itens de n itens sem repetição e sem ordem.
#print('O valor é {}' .format(teste12))

#teste13 = math.copysign(n1)
#copysign(x, y)
#Retorna um ponto flutuante com a magnitude (valor absoluto) de x, mas o sinal de y. Em plataformas que suportam zeros sem sinal, copysign(1.0, -0.0) retorna -1.0.
#print('O valor é {}' .format(teste13))

teste14 = math.cos(n1)
#Retorna o cosseno de x radianos.
print('O valor de cos é {:.2f}' .format(teste14))

#teste16 = math.factorial(n1)
#Retorna o fatorial de n como um inteiro. Levanta ValueError se n não for um inteiro ou for negativo.
# 27 = Retorna Erro
#print('O valor é {}' .format(teste16))

teste17 = math.floor(n1)
#Retorna o limite mínimo de x, o maior inteiro menor ou igual a x. Se x não é um ponto flutuante, delega para x.__floor__, cujo qual deve retornar um valpr dp tipo Integral
print('O valor floor / parte inteira é {}' .format(teste17))

#teste18 = math.fsum(n1)
#fsum(iterable)
#Retorna uma soma de valores de ponto flutuante precisa no iterável. Evita perda de precisão rastreando várias somas parciais intermediárias:
#print('O valor é {}' .format(teste18))

#teste19= math.gcd(n1)
#gcd(*integers)
#Retorna o maior divisor comum dos argumentos inteiros especificados. Se algum dos argumentos for diferente de zero, o valor retornado será o maior inteiro positivo que é um divisor de todos os argumentos. Se todos os argumentos forem zero, o valor retornado será 0. gcd() sem argumentos retorna 0.
#print('O valor é {}' .format(teste19))

#teste20 = math.infinite(n1)
#Retorna True se x não for um infinito nem um NaN, e False caso contrário. (Observe que 0.0 é considerado finito.)
#print('O valor é {}' .format(teste20))

teste21 = math.isinf(n1)
#Retorna True se x for um infinito positivo ou negativo, e False caso contrário.
print('O valor isinf é {}' .format(teste21))

# teste23 = math.isqrt(n1)
#Retorna a raiz quadrada inteira do inteiro não negativo n. Este é o piso da raiz quadrada exata de n, ou equivalentemente o maior inteiro a tal que a² ≤ n.
# Não está funcionando, pois o número n1 está sendo convertido como flutuante
# print('O valor é {}' .format(teste23))

teste24 = math.modf(n1)
#Retorna as partes fracionárias e inteiras de x. Ambos os resultados carregam o sinal de x e são pontos flutuantes.
print('O valor modf é {}' .format(teste24))

teste25 = math.trunc(n1)
#Retorna x com a parte fracionária removida, deixando a parte inteira. Isso arredonda para 0: trunc() é equivalente a floor() para x positivos, e equivalentes a ceil() para x negativos. Se x não é um ponto flutuante, então delega para x.__trunc__, cujo qual deve retornar um valor do tipo Integral.
print('O valor trunc é {}' .format(teste25))

teste26 = math.ulp(n1)
#Retorna o valor do bit menos significativo do ponto flutuante x:
#Se x for um NaN (não um número), retorna x.
#Se x for negativo, retorna ulp(-x).
#Se x for um infinito positivo, retorna x.
#Se x for igual a zero, retorna o menor valor flutuante positivo desnormalizado representável (menor que o ponto flutuante de valor mínimo positivo normalizado, sys.float_info.min).
#Se x for igual ao maior ponto flutuante positivo representável, retorna o valor do bit menos significativo de x, tal que o primeiro ponto flutuante menor que x seja x - ulp(x).
#Caso contrário (x é um número finito positivo), retorna o valor do bit menos significativo de x, de modo que o primeiro ponto flutuante maior que x seja x + ulp(x).
print('O valor ulp é {}' .format(teste26))

teste28 = math.exp(n1)
#Retorna e elevado à potência x, onde e = 2.718281… é a base dos logaritmos naturais. Isso geralmente é mais preciso do que math.e ** x ou pow(math.e, x).
print('O valor exp é {}' .format(teste28))

teste29 = math.exp2(n1)
#Retorna 2 elevado a x
print('O valor exp 2 / 2 elevado ao número é igual a {}' .format(teste29))

teste30 = math.expm1(n1)
#Retorna e elevado à potência x, menos 1. Aqui e é a base dos logaritmos naturais. Para pequenos pontos flutuantes x, a subtração em exp(x) - 1 pode resultar em uma perda significativa de precisão; a função expm1() fornece uma maneira de calcular essa quantidade com precisão total:
print('O valor expm1 é {}' .format(teste30))

#teste31 = math.log1p(n1)
#Retorna o logaritmo natural de 1+x (base e). O resultado é calculado de forma precisa para x próximo a zero.
#Quando x <= -1, o argumento da função log1p é negativo, o que resulta em uma exceção "math domain error". Portanto, é importante garantir que o valor de x seja maior que -1 antes de aplicar a função log1p.
#print('O valor é {}' .format(teste31))

#teste32 = math.log2(n1)
#Retorna o logaritmo de base 2 de x. Isso geralmente é mais preciso do que log(x, 2).
##Quando x <= -1, o argumento da função log1p é negativo, o que resulta em uma exceção "math domain error". Portanto, é importante garantir que o valor de x seja maior que -1 antes de aplicar a função log1p.
#print('O valor é {}' .format(teste32))

#teste33 = math.log10(n1)
#Retorna o logaritmo de base 10 de x. Isso geralmente é mais preciso do que log(x, 10).
##Quando x <= -1, o argumento da função log1p é negativo, o que resulta em uma exceção "math domain error". Portanto, é importante garantir que o valor de x seja maior que -1 antes de aplicar a função log1p.
#print('O valor é {}' .format(teste33))

#teste34 = math.sqrt(n1)
#Retorna a raiz quadrada de x.
##Quando x <= -1, o argumento da função log1p é negativo, o que resulta em uma exceção "math domain error". Portanto, é importante garantir que o valor de x seja maior que -1 antes de aplicar a função log1p.
#print('O valor é {}' .format(teste34))

#teste35 = math.acos(n1)
#Retorna o arco cosseno de x, em radianos. O resultado está entre 0 e pi.
# 27 = Retorna erro
#print('O valor é {}' .format(teste35))

#teste36 = math.asin(n1)
#Retorna o arco seno de x, em radianos. O resultado está entre -pi/2 e pi/2.
#print('O valor é {}' .format(teste36))

teste39 = math.sin(n1)
#Retorna o seno de x radianos.
print('O valor é {}' .format(teste39))

teste40 = math.tan(n1)
#Retorna o tangente de x radianos.
print('O valor da tangente em radianos é {}' .format(teste40))

teste41 = math.degrees(n1)
#Converte o ângulo x de radianos para graus.
print('O valor é {}' .format(teste41))

teste42 = math.radians(n1)
#Converte o ângulo x de graus para radianos.
print('O valor é {}' .format(teste42))

#teste43 = math.acosh(n1)
#A função cosseno hiperbólico inverso (acosh) é uma função matemática que retorna o arco cosseno hiperbólico inverso de um número. É definida como: acosh(x) = ln(x + sqrt(x^2 - 1)), onde sqrt é a raiz quadrada.
#Note que o argumento da função acosh deve ser maior ou igual a 1, caso contrário a função não está definida para esse valor.
#print('O valor é {}' .format(teste43))

teste44 = math.asinh(n1)
#A função seno hiperbólico inverso (asinh) é uma função matemática que retorna o arco seno hiperbólico inverso de um número. É definida como: asinh(x) = ln(x + sqrt(x^2 + 1)), onde sqrt é a raiz quadrada. A função asinh é útil em muitas aplicações, incluindo geometria, física e cálculo. O intervalo de valores para x na função asinh é todo o conjunto de números reais. Portanto, x pode ser qualquer número real, positivo ou negativo, incluindo 0.
print('O valor é {}' .format(teste44))

#teste45 = math.atanh(n1)
#Retorna a tangente hiperbólica inversa de x.
# Pra funcionar precisa ser um valor entre -1 e 1 
# Exemplo : 0.5 , -0.5
#print('O valor é {}' .format(teste45))

teste47 = math.sinh(n1)
#Retorna o seno hiperbólico de x.
print('O valor seno é {:.2f}' .format(teste47))

teste48 = math.tanh(n1)
#Retorna a tangente hiperbólica de x.
print('O valor é {}' .format(teste48))

teste49 = math.erf(n1)
#Retorna a função erro em x.
print('O valor é {}' .format(teste49))

teste50 = math.erfc(n1)
#Retorna a função erro complementar em x. A função erro complementar é definida como 1.0 - erf(x). É usado para grandes valores de x onde uma subtração de um causaria uma perda de significância.
print('O valor é {}' .format(teste50))

#teste51 = math.gamma(n1)
#A função gama (γ) é uma função matemática que representa a função gama completa. Ela é utilizada em muitas áreas, incluindo probabilidade, estatística e cálculo numérico. A função gama é definida como: Γ(x) = (x-1)! para x inteiro positivo, onde ! representa o fatorial. Para valores de x que não são inteiros positivos, a função gama é definida como a solução para a integral de t^(x-1)e^-t dt de 0 a infinito. O intervalo de valores para x na função gama é todo o conjunto de números reais positivos.
#Retorna a função gama em x.
#print('O valor é {}' .format(teste51))

#teste52 = math.lgamma(n1)
#Retorna o logaritmo natural do valor absoluto da função gama em x.
#A função logaritmo gama (lgamma) é uma função matemática que retorna o logaritmo natural (ln) da função gama (γ). É definido como: lgamma(x) = ln(Γ(x)). A função lgamma é útil em muitas aplicações, incluindo probabilidade, estatística e cálculo numérico, pois evita problemas de precisão numérica que podem ocorrer ao calcular diretamente o logaritmo de números muito grandes. O intervalo de valores para x na função lgamma é todo o conjunto de números reais positivos.
#print('O valor é {}' .format(teste52))
