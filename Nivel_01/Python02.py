# 02:
# Cria Script que leia o nome da pessoa e mostre uma mensagem de 2 formas diferentes

print('1-Criar Script que leia o nome da pessoa e mostre uma mensagem') 
print('de Boas-Vindas de acordo com a mensagem digitada')
input('Qual é o seu nome ? ')
nome = input('Qual e o seu nome ? ')
print('Olá',nome,',seja bem-vindo !')
print('Olá {}, seja bem-vindo !'. format(nome))

#In Python we declare the variable in the text
#In Python what comes from a box is text (called a string), so we must convert it to an integer, real or boolean number, if we want the program to identify it we will have to use conditional operators or we can convert it to text at the end
# In Python we use "," comma instead of +, because "+" concatenates
n0 = input("Enter a number: ")
print(type(n0))
n1 = int(input("Enter another number: "))
n2 = int(input('Enter another number : '))
soma12 = n1 + n2
print('The sum of ' , n1 , '+' , n2 , 'is' , soma12)
print('The sum of' + str(n1) + ' + ' + str(n2) + ' is ' + str(soma12))
# 
# 
print('The sum of ' , n1 , '+' , n2 , 'is' , soma12)
print('The sum of ' , n1 , '+' , n2 , 'is' , soma12)
print('The sum of ' , n1 , '+' , n2 , 'is' , soma12)

# msg1 = Testando
# print(msg1)
# A variável não reconhece a string

#msg2 = Oi voce
#print(msg2)
# A variável não reconhece a string

#msg3 = 2
#print("O valor de msg3 é : " + msg3)

#A mensagem de erro "can only concatenate str (not 'int') to str" ocorre quando você está tentando concatenar (juntar) uma string com um valor inteiro em Python usando o operador de adição (+) direto. Em Python, você não pode concatenar diretamente uma string com um número inteiro, a menos que você converta o número inteiro em uma string antes de realizar a concatenação.

#msg4 = +
#print(msg4)
# Essa mensagem de erro indica que o compilador ou interpretador estava esperando encontrar uma expressão válida em um determinado ponto do código, mas não encontrou o que esperava.

msg5 = 1 + 1 # Adição
print("O valor de msg5 é : " + str((msg5)))
# A mensagem de erro "can only concatenate str (not 'int') to str" em Python ocorre quando você está tentando concatenar (juntar) uma string com um valor inteiro usando o operador de adição (+) direto, mas a operação não é permitida. Isso acontece porque, em Python, você não pode concatenar diretamente uma string com um número inteiro sem convertê-lo em uma string primeiro.
print(msg5)

# Operações :
#soma = n2 + n1
#sub = n2 - n1
#mult = n2 * n1
#div = n2 / n1
#divInt = n2 // n1
#resto = n2 % n1
#pot = n2 ** n1

msg6 = 1 - 1 # Subtração
print(msg6)

msg7 = 1 * 1 # Multiplicação
print(msg7)

msg8 = 1 / 1 # Divisão
print(msg8)

msg9 = 4 // 2 # Divisão Inteira ou Divisor
print(msg9)
# Dividendo | Diviso
# Resto     | Quociente

msg10 = 1 % 1 # Resto da Divisão
print(msg10)

msg11 = 1 ** 1 # Potenciação
print(msg11)

msg12 = 1 ** ( 1/2 ) # Raiz Quadrada
print(msg12)

msg13 = 2 ** ( 3/3 )
print(msg13)

# 1/2 : Numerador 1 
#       Denominador 2

# 1 elevado a 1/2  = Raiz Quadrada de 1 > 1
# 4 elevado a 1/2  = ... ... de 4 > 2
# 27 elevado a 1/3 = ... Cúbica de 27 > 3
#  2 elevado a 2/3 = ... ... de 2 elevado a 2
# Resposta : raiz cúbica de 4
#  2 elevado a 3/3 = ... ... de 2 elevado a 3
# Resposta : 2³ = 2 x 2 ( 4 ) x 2 ( 8 ) > 2
#  2 elevado a 4/3 = ... ... de 2 elevado a 4
# Resposta : 2 x 2 ( 4 ) x 2 ( 8 ) x 2 ( 16 ) 

