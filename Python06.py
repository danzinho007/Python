print('3-Criar Script que leia dois números e tente mostrar a soma')
print('entre eles')
n1 = input('Digite o 1° número : ')
print(type(n1))
n2 = int(input('Digite o 2° número : ')) # int(input) Converte a string em número
print(type(n2))
n3 = int(input('Digite o 3° número : '))
print(type(n3))
#s1 = n1 + n2 < Erro pois o valor n1 é um string
s2 = n2 + n3
print('A soma vale ', s2) 
print('A soma entre', n2, 'e', n3, 'vale', s2)
print('A soma entre {} e {} vale {}' .format(n2, n3, s2))
print('A soma entre {0} e {1} vale {2}' . format(n2, n3, s2))
