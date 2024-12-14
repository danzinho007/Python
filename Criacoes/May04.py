print("\n Create a program that reads two numbers and displays the sum, subtraction, multiplication, division, integer division, exponentiation and modulus between them.. \n")

n1 = int(input('Enter a number: '))
# Recebe algo, converte pra inteiro e guarda na variável first_number
n2 = int(input('Enter another number: '))

print("\nSum")
print(f'The sum of {n1} + {n2} is equal to {n1 + n2}.\n')

print("Subtraction")
print(f'The subtraction of {n1} and {n2} is equal to {n1 - n2}.\n')

print("Multiplication")
print(f'The multiplication of {n1} and {n2} is equal to {n1 * n2}.\n')

print("Division")
print(f'The subtraction of {n1} and {n2} is equal to {n1 / n2:.2f}.\n')
# :.2f indica que o número será formatado com 2 casas decimais no formato de ponto flutuante, ou seja, 2 casas depois da vírgula

print("Integer Division")
print(f'The integer division of {n1} and {n2} is equal to {n1 // n2}.\n')

print("Exponentiation")
print(f'The exponentiation of {n1} and {n2} is equal to {n1 ** n2}.\n')

print("Module")
print(f'The module of {n1} and {n2} is equal to {n1 % n2}.\n')

print(type(n1)) 
# Mostra o tipo da variável n1

print("\n Or : ") 

sum = n1 + n2
print(f"The sum of {n1} + {n2} is equal to {sum}.")

print("\n Or : ") 

n3 = int(input("Digite um número: "))
n4 = int(input("Digite outro número: "))
soma = n3 + n4
print("A soma de " + str(n3) + " + " + str(n4) + " é " + str(soma))
# Concatenação funciona apenas para strings
# Ela converte para string somente para o print, o número continua sendo inteiro

print(type(n3))
# Mostra o tipo da variável n3
