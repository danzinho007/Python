print(" Write a program that reads the length of the opposite and adjacent sides of a right triangle. Calculate and show the length of the hypotenuse.")
print("Escreva um programa que leia o comprimento dos lados opostos e adjacentes de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.")

# Relembrando :
# Hipotenusa ao quadrado é igual a soma dos catetos ao quadrado
# h² = l² + l² ou h = Raiz quadrada de l² + l²

ladoA=float(input("Informe o lado oposto : "))
ladoB=float(input("Informe o lado adjacente : "))
print(f"A hipotenusa mede : {(ladoA**2 + ladoB**2) **(1/2)}")
