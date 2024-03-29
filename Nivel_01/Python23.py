#Desafios

# 15- Escreva um programa que pergunte a quantidade Km percorridos por um carro alugado e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia com 0,15 Km rodado

dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos Km rodados ? '))

pago = ( dias * 60 )  + ( km * 0.15)
print('O total a pagar é de R${:.2f}' .format(pago))
