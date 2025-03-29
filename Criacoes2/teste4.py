# Teste 2

import re

dados2 = input("Escreva algo aqui: ")

# Encontrar todas as sequências de números seguidas por letras, ignorando os zeros no final
matches2 = re.findall(r'\d+[A-Za-z](?=\d*[^0])|\d+[A-Za-z]', dados2)

# Filtrar as sequências que não sejam seguidas apenas de zeros
matches2 = [match2.rstrip('0') for match2 in matches2]

print("Números filtrados:", matches2)
