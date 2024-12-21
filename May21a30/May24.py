print("Create a program that reads the name of a city and says whether or not it starts with the name 'Saint'.")
print("Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Saint'.")

city = input('\nWhat city were you born ? ')
city = ' '.join(city.strip().split()).title()

# Pega os 5 primeiros caracteres, coloca tudo pra maiúsculo e verifica se é igual a SAINT :
print(city[:5].upper() == 'SAINT')
print(f"A cidade {city} começa com Saint ? {city[:5].upper() == 'SAINT'}\n")
