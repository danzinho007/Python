print("\nCreate an algorithm that reads the price of a product and shows its new price with a 15% discount")

# Calculando
# Produto  - Porcentagem
# R$ x - 100%
# R$ y - 15%
# Logo pra saber o novo preço de um produto com 15% de desconto será :
# Preço do produto - ( Preço do produto * 15 / 100 )

price = float(input("\nInforme o preço do produto : "))
print(f"O desconto de 15% de um produto que custa {price} é de R$ {(price*15)/100} reais")
print(f"O valor final do produto será R$ {price - (price*15)/100} reais")