print("\n Create a program that reads two numbers and displays the sum between them. \n")

n1 = int(input('Enter a number: '))
# Recebe algo, converte pra inteiro e guarda na variável first_number
n2 = int(input('Enter another number: '))

print(f'The sum of {n1} + {n2} is equal to {n1 + n2}.')
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
