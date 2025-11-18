#26- Write a program that reads a sentence from the keyboard and shows how many times the letter "a" appears and in what position it is
# appears the first time and in what position it appears last time.
 
#26- Escreva um programa que leia uma frase do teclado e mostre quantas vezes a letra "a" aparece e em que posição ela está aparece na primeira vez e em que posição ela aparece na última vez.

# Solicitando uma palavra e convertendo ela pra maiúsculo :
sentence = input('Enter a sentence : ').upper()

# Verificando quantos A aparece na palavra :
print(f'The letter A shows {sentence.count("A")} times.')

# Procurando o primeiro A da palavra :
print(f'The first letter A shows in position {sentence.find("A")+1}.')

# Procurando o segundo A da palavra :
print(f'O segundo A aparece na posição : {sentence.find("A", sentence.find("A") + 1) + 1}.')

# Procurando o último A da palavra :
print(f'The last letter A shows in position {sentence.rfind("A")+1}.')
