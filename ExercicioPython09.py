#Desafios

# 14- Escrever um programa que converte de °C para °F

c = float(input('Informe a temperatura em °C : '))

f = (( 9 * c) / 5 ) + 32
#ou#
f1 = 9 * c / 5 + 32
#Ordem de Precedência :
#Multiplicação e Divisão é o que vier primeiro

print('A temperatura de {}°C corresponde a {}°F' .format(c, f))
print('A temperatura de {}°C corresponde a {}°F' .format(c, f1))

# 15- Escreva um programa que pergunte a quantidade Km percorridos por um carro alugado e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia com 0,15 Km rodado

dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos Km rodados ? '))

pago = ( dias * 60 )  + ( km * 0.15)
print('O total a pagar é de R${:.2f}' .format(pago))
