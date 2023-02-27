#!!! Desafios : 
#005 : Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor

print('Saiba aqui o Antecessor e o Sucessor de qualquer número')
#Irá mostrar na tela a Mensagem
nAtual = int(input('Digite aqui o valor : '))
#Esse comando irá monstrar a mensagem, esperar uma resposta do usuário, após isso irá converter a resposta em número inteiro
nAnt = nAtual - 1
nSuc = nAtual + 1
input('O antecessor de {} é {}, \n e o sucessor de {} é {}' .format(nAtual, nAnt, nAtual, nSuc))
#ou
input('O antecessor de {} é {}, \n e o sucessor de {} é {}' .format(nAtual, (nAtual -1), nAtual, (nAtual + 1)))

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

#007 : Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra sua média

print(' ')
print('Saiba aqui a sua média')
n2 = int(input('Digite aqui quanto você tirou no Teste : '))
n3 = int(input('Digite aqui quanto você tirou na Prova : '))
media = ( n2 + n3 ) / 2
input('A média do aluno que tirou {:.1f} com {:.1f} é {:.1f}' .format(n2, n3, media))
#ou
input('A média do aluno que tirou {:.1f} com {:.1f} é {:.1f}' .format(n2, n3, ((n2 + n3) / 2)))

#008 : Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm

print(' ')
# km hm dam m dm cm mm
# 1  0   0  0  0  0  0 = 1 km tem 10 hm, 100 dam ou 1.000 m
# 0  0   0  1  0  0  0 = 1  m tem 10 dm, 100  cm ou 1.000 mm
# 0, 0   0  0  0  0  1 = 1 mm tem 0,000.001 km
# 0  0   0  0, 0  0  1 = 1 mm tem 0,001 m

print('Saiba aqui quantos dm, cm e mm tem qualquer metro')
n4 = int(input('Digite aqui o valor : '))
dm = n4 * 10
cm = n4 * 100
mm = n4 * 1000
input('A medida de {} é de {:.0f} dm, {:.0f} cm e {:.0f}mm' .format(n4, dm, cm, mm))

#009 : Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

print(' ')
print('Saiba aqui a Tabuada de 1 até 10 de qualquer número')
n5 = int(input('Digite aqui o número : '))
x01 = n5 * 1
x02 = n5 * 2
x03 = n5 * 3
x04 = n5 * 4
x05 = n5 * 5
x06 = n5 * 6
x07 = n5 * 7
x08 = n5 * 8
x09 = n5 * 9
x10 = n5 * 10
input('A tabuada de {} é : {} x {} = {} \n {} x {} = {} \n {} x {} = {} \n {} x {} = {} \n {} x {} = {} \n {} x {} = {} \n {} x {} = {} \n {} x {} = {} \n {} x {} = {} \n {} x {} = {}' .format(n5, n5, 1, x01, n5, 2, x02, n5, 3, x03, n5, 4, x04, n5, 5, x05, n5, 6, x06, n5, 7, x07, n5, 8, x08,n5, 9, x09,n5, 10, x10))

#ou

print('-' * 12)
print('{} x {:2} = {}' .format(n5, 1, n5 * 1))
print('{} x {:2} = {}' .format(n5, 2, n5 * 2))
print('{} x {:2} = {}' .format(n5, 3, n5 * 3))
print('{} x {:2} = {}' .format(n5, 4, n5 * 4))
print('{} x {:2} = {}' .format(n5, 5, n5 * 5))
print('{} x {:2} = {}' .format(n5, 6, n5 * 6))
print('{} x {:2} = {}' .format(n5, 7, n5 * 7))
print('{} x {:2} = {}' .format(n5, 8, n5 * 8))
print('{} x {:2} = {}' .format(n5, 9, n5 * 9))
print('{} x {:2} = {}' .format(n5, 10, n5 * 10))
print('-' * 12)

#010 : Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considera U$$1.00 = R$ 3.27
#011 : Faça um programa que leia a largura e a altura de uma parede em m, calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
#012 : Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
#013 : Faça um algoritmo que leia o salário de um funcionário e mostra seu novo salário com 15% de aumento
