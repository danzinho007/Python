#27- Write a program that reads a person's full name, then shows the first and last names separately.
 
#27- Escreva um programa que leia o nome completo de uma pessoa e depois mostre o primeiro e o último nome separadamente.

# Pedindo o nome, guardando na variável e depois removendo os espaços  no início e no final da string :
nomeCompleto = input("Digite seu nome completo: ").strip()

# Transforma o nome completo em uma string com capitalização correta
nome = ' '.join(palavra.title() for palavra in nomeCompleto.split())

# Dividindo o nome em uma lista de palavras
nomeDividido = nome.split()

# Extraindo o primeiro e o último nome
primeiroNome = nomeDividido[0]
ultimoNome = nomeDividido[-1]

# Exibindo o resultado
print(f"Seu primeiro nome é: {primeiroNome}")
print(f"Seu último nome é: {ultimoNome}")
