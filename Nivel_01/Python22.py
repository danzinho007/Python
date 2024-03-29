# 14- Escrever um programa que converte de °C para °F

c = float(input('Informe a temperatura em °C : '))

f = (( 9 * c) / 5 ) + 32
#ou#
f1 = 9 * c / 5 + 32
#Ordem de Precedência :
#Multiplicação e Divisão é o que vier primeiro

print('A temperatura de {}°C corresponde a {}°F' .format(c, f))
print('A temperatura de {}°C corresponde a {}°F' .format(c, f1))
