from string import ascii_uppercase

# Lista de letras do alfabeto
letras = list(ascii_uppercase)

# Loop aninhado para gerar as combinações
for letra1 in letras:
    for letra2 in letras:
        combinacao = letra1 + letra2
        print(combinacao)
