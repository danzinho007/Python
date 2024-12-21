print("\nBiblioteca random : ")

import random

frutas = ["maçã", "banana", "laranja", "uva", "manga"]
escolhida = random.choice(frutas)
print(f"A fruta escolhida é: {escolhida}")

resultado = random.choice(["Cara", "Coroa"])
print(f"O resultado do cara ou coroa é: {resultado}")

numero = random.randint(1, 100)
print(f"O número sorteado entre 1 e 100 é: {numero}")

dado = random.randint(1, 6)
print(f"Você lançou o dado e tirou: {dado}")

nomes = ["Ana", "João", "Carlos", "Mariana", "Pedro", "Sofia"]
vencedores = random.sample(nomes, 3)  # Escolhe 3 vencedores sem repetição
print(f"Os vencedores do sorteio são: {', '.join(vencedores)}")

cartas = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Rainha", "Rei"]
random.shuffle(cartas)
print(f"As cartas embaralhadas são: {cartas}")

numero = random.uniform(1.5, 6.5)
print(f"O número decimal sorteado entre 1.5 e 6.5 é: {numero:.2f}")