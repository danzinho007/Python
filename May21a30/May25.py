print("\nCreate a program that reads a person's name and tells if they have Silva' in their name")
print("Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva' no nome")

nome = input("Qual é o seu nome ? ")
nome = ' '.join(nome.strip().split()).title()

# Converte a string nome para minúscula e verifica se tem silva em algum lugar : 
print(f"O nome {nome} tem Silva em algum lugar ? {'silva' in nome.lower()}")

# Verifica se tem Silva no nome : 
print(f"O nome {nome} tem Silva em algum lugar ? {'Silva' in nome}")

# Acessando o 2° nome da variável, jogando tudo pra minúsculo e verificando se tem silva ?
print(f"O nome {nome} tem Silva no sobrenome ? {'silva' == nome.split()[1].lower()}")

# Acessando o 2° nome da variável, jogando tudo pra minúsculo e verificando se tem silva no último nome :
print(f"O nome {nome} tem Silva no último nome ? {'silva' == nome.split()[-1].lower()}")
