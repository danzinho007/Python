print("\nCreate a program that reads how much money a person has in their wallet and shows how many dollars they can buy.")
# Site usado : https://www.melhorcambio.com/peso-argentino-hoje

# 1 iene           = 0.0396 reais
# 1 peso argentino = 0.0060 reais
# 1 dólar          = 6.04 reais

# 1 dólar = 5.45 reais
# x = 5.45 
# x = 5.45 / 5.45  > x = 1 dólar

reais=float(input("\nDigite o valor em reais : R$ "))
print(f"O valor {reais} reais em dólar é {reais / 6.04:.2f}")
print(f"O valor {reais} reais em ienes é {reais / 0.0396:.2f}")
print(f"O valor {reais} reais em pesos argentinos é {reais / 0.0060:.2f}\n")

# Agora ao contrário
dolar=float(input("\nDigite o valor em dólares : $ "))
print(f"O valor {dolar} dólares em reais é {dolar * 6.04:.2f}\n")
