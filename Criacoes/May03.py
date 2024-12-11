# Create a program that asks for the user's name and writes a welcome message.

name = input('What is your name: ')
# Guardando algo na variável name usando o comando input

print(f'Nice meet you, {name}!')  # Caso 1
print('Nice meet you, {}!'.format(name)) # Caso 2
print('Nice meet you, ' + name,"!") # Caso 3

# OBS : Tanto faz aspas simples ('') quanto aspas duplas ("")

# Caso :
# 1 = f-String : Formatando a string desde o começo
# 2 = str.formato : Formatando a string depois
# 3 = Concatenando string

# Recomendado : 1, 2 ou 3
