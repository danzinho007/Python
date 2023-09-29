import random
def gera():
    return random.randint(1, 100)
def game():
    return gera()

resposta = gera()
tentativa = 0
print("palpite gerado")
chute = 0

while chute is not resposta:
    tentativa += 1
chute = int(input("Qual é o seu chute ? "))
if chute > resposta:
    print("Errou ! É um valor menor que o chute")
else:
    print("Parabéns ! O número gerado está certo")
    while True:
        game()

#Bugado