#29- Write a program that reads the speed of a car. If it exceeded 80km/h, show a message saying that it was fined. The fine will cost R$7.00 for each km above the limit.

#29- Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa custará R$ 7,00 para cada km acima do limite.

velocidade = float(input("Digite a velocidade em km/h : "))
multa = velocidade * 7

if velocidade <= 80 :
    print("Sem multa")
else :
    print(f"Você foi multado, pois estava a {velocidade}")
    print(f"Pague : {multa:.2f}")

# Exemplo : 80 ( sem multa ) e 85 
#  85 
# x 7
# 595
