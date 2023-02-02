#Testando operações

n1 = int(input('Digite um valor : '))
n2 = int(input('Digite outro valor :'))

print('Para n1 temos : ')
soma1 = n1 + n2
print('A soma vale {}' . format(n1+n2))
sub1 = n1 - n2
multi1 = n1 * n2
print('A subtração é {} e a multiplicação é {}' . format(sub1, multi1))

divi1 = n1 / n2
print('A Divisão é {:.3f}' .format(divi1), end= ' ')
print('A Divisão é {:.2f}' .format(divi1), end= ' >>> ')
print('A Divisão é {:.1f}' .format(divi1))
pote1 = n1 ** n2
divInt1 = n1 // n2
resto1 = n1 % n2
print('A divisão vale {}, \n a potência vale {}, \n a divisão inteira vale {} \n e o resto da divisão é {}' .format(divi1, pote1, divInt1, resto1))

print('Para n2 temos : ')
soma2 = n2 + n1
sub2 = n2 - n1
multi2 = n2 * n1
divi2 = n2 / n1
pote2 = n2 ** n1
divInt2 = n2 // n1
resto2 = n2 % n1
