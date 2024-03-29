# Testando operações pra n2

print('Testando operações para n2')
n1 = int(input('Digite o primeiro valor : '))
n2 = int(input('Digite o segundo valor : '))

print('Para n2 temos : ')
soma = n2 + n1
sub = n2 - n1
mult = n2 * n1
div = n2 / n1
divInt = n2 // n1
resto = n2 % n1
pot = n2 ** n1

print('Sendo {} e {} temos : ' .format(n2, n1))
print('A soma vale {}' .format(soma))
print('A subtração é {}' .format(sub))
print('A multiplicação é {}' .format(mult))
print('A Divisão é {}' .format(div))
print('A Divisão Inteira / Quociente é {}' .format(divInt))
print('O Resto da Divisão é {}' .format(resto))
print('A Potenciação é {}' .format(pot))
