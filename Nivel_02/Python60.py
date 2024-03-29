# 24 
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

city = str(input("Em que cidade você nasceu ? "))
print(city[0:5].upper() == "SANTO" ) # Ou print(city[:5])
