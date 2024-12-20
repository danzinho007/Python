print("\nThe same teacher from challenge 19 wants to draw the order in which the students' work will be presented. Make a program that read the names of the four students and show the order drawn.")

print("\nO mesmo professor do desafio 19 quer desenhar a ordem em que os trabalhos dos alunos serão apresentados. Faça um programa que leia os nomes dos quatro alunos e mostre a ordem desenhada.")

aluno1=input("Informe o nome do 1° aluno : ")
aluno2=input("Informe o nome do 2° aluno : ")
aluno3=input("Informe o nome do 3° aluno : ")
aluno4=input("Informe o nome do 4° aluno : ")

list = [aluno1, aluno2, aluno3, aluno4]
list.sort()
print(f"Lista ordenada : {list}")
