print("\nDevelop a program that reads a student's two grades, calculates and displays their average.")

# Perguntando, convertendo o conteúdo pra real e guardando na variável teste :
print("O número deve ser digitado de forma inteira (8) ou decimal (6.72")
print("Não use vírgulas !!!")

# teste : 6.72 com 8 > 14.72 / 2 é 1472 / 200
# 1472  | 200
#   7   | 7.36
#   12  |
#    0  |

teste=float(input("\nQual foi a nota do teste ? "))
prova=float(input("Qual foi a nota da prova ? "))
print(f"A média de {teste} e {prova} é de {(teste + prova) / 2 :.2f}\n")
