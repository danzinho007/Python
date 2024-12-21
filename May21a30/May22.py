print("\nCreate a program that reads a person's full name and displays :")
# - The name in all upper and lower case letters.
# - How many letters in total without considering spaces
# - How many letters are in the first name.

name=input("\nDigite um nome : ")
# Removendo os espaços, juntando e dando 1 espaço entre cada palavra :
name = ' '.join(name.strip().split()).title()
# ' '.join(): Junta as palavras da lista em uma única string, separadas por um único espaço.
# strip(): Remove espaços no início e no final da string.
# split(): Divide a string em uma lista de palavras, ignorando os espaços extras.
# capitalize(): Aplica a capitalização apenas na primeira palavra (o restante fica em minúsculas).

print(f"Analizando {name}")
print(f"Seu nome com letras grandes fica : {name.upper()}")
print(f"Seu nome com letras pequenas fica : {name.lower()}")
print(f"Seu nome tem : {len(name) - name.count(' ')} letras\n")
