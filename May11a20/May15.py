print("# Write a program that asks the number of km traveled by a rented car and the number of days for which it was rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven.")

print("# Escreva um programa que pergunte o número de km percorridos por um carro alugado e o número de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.")

#  Km - Dias - Preço
# 0,15    1      60
# Exemplo : Rodei 30km em 2 dias
# 1 dia  = 60
# 2 dias = x >>> x = 120
# 1  km = 0.15
# 30 km = x >>> x = 30 . 15/100
# x = 450/100 > x = 4.5 
# Total : Dias + km > 120 + 4.50 > 124.50
# Logo o preço é : Dias percorridos * 60 + km * 0,15

km = float(input("\nQuantos km o carro rodou ? "))
dia = int(input("Quantos dias você rodou com ele ? "))
print(f"O preço a pagar será de R$ {(dia * 60 + km * 0.15 ):.2f}")
