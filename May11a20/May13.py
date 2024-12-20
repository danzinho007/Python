print("\nMake a program that reads an employee's salary and shows his new salary with a 15% increase.")

# Calculando
# Produto  - Porcentagem
# R$ x - 100%
# R$ y - 15%
# Logo pra saber o novo preço de um produto com aumento de 15% será :
# Preço do produto + ( Preço do produto * 15 / 100 )

price = float(input("\nInforme o preço do produto : "))
print(f"O aumento de 15% de um produto que custa {price} é de R$ {(price*15)/100} reais")
print(f"O valor final do produto será R$ {price + (price*15)/100} reais")
