#!!! Desafios : 
#005 : Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor

print('Saiba aqui o Antecessor e o Sucessor de qualquer número')
#Irá mostrar na tela a Mensagem

nAtual = int(input('Digite aqui o valor : '))
#Esse comando irá monstrar a mensagem, esperar uma resposta do usuário, após isso irá converter a resposta em número inteiro

nAnt = nAtual - 1
nSuc = nAtual + 1
input('O antecessor de {} é {}, \n e o sucessor de {} é {}' .format(nAtual, nAnt, nAtual, nSuc))
#ou
input('O antecessor de {} é {}, \n e o sucessor de {} é {}' .format(nAtual, (nAtual -1), nAtual, (nAtual + 1)))

