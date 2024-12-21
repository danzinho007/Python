print("\nFunções : ")

# Funcão com argumento msg
print("\nExemplo 01 :")
def funcao1 (msg):
    print(msg)
funcao1("Teste")

print("\nExemplo 02 :")
def funcao2 (msg, nome):
    print(msg, nome)
funcao2("Olá", "Daniel")
funcao2("Olá", "Raquel")

print("\nExemplo 03 : ")
def funcao3 (msg, nome):
    print(msg)
funcao3("Olá", "Daniel")

print("\nExemplo 04 :")
def funcao4 (msg="Olá", nome="Daniel"):
    print(msg, nome)
funcao4()
funcao4("Raquel", "Olá")
funcao4("Raquel", nome="Olá")
funcao4(nome="Raquel", msg="Olá")

print("\nExemplo 05 :")
def funcao5 (msg="Olá", nome="Daniel"):
    msg = msg.replace("e", "3")
    nome = nome.replace("e", "3")
    print(msg, nome)
funcao5()
funcao5("Raquel", "Olá")
funcao5("Raquel", nome="Olá")
funcao5(nome="Raquel", msg="Olá")
