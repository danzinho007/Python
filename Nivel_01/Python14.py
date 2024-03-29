# Executar com F5

#006 : Criei um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print(' ')
print('Saiba aqui o Dobro, Triplo, Quádruplo, Quintuplo e a Raiz \n Quadrada de Qualquer Número')
n1 = int(input('Digite aqui o valor : '))

dobro = n1 * 2
triplo = n1 * 3
quad = n1 * 4
quint = n1 * 5
raiz = n1 ** ( 1/2 )

input('O dobre de {} é {}, \n o triplo de {} é {}, \n o quádruplo de {} é {}, \n o quintúplo de {} é {} \n e a Raiz Quadrada de {} é {:.2f}' .format(n1, dobro, n1, triplo, n1, quad, n1, quint, n1, raiz))

#:.2f = 2 casas após a vírgula
input('A raiz quadrada de {} vale {:.2f}' .format(n1, pow(n1, (1/2))))


