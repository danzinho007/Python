# Jogo de Advinhar número gerado de 1 a 100 contando todas tentativas

import random
def gera():
    return random.randint(1, 100)
def game():
    return gera()

resposta = game()
tentativa = 0
print("palpite gerado")

while True:
    chute = int(input("Qual é o seu chute? "))
    tentativa += 1
    if chute > resposta:
        print("Errou! É um valor menor que o chute")
    elif chute < resposta:
        print("Errou! É um valor maior que o chute")
    else:
        print(f"Parabéns! Você acertou em {tentativa} tentativas. O número gerado estava certo.")
        break  # Sai do loop quando a resposta é correta

#Correto
