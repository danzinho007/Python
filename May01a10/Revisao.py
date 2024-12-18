import colorama
colorama.init()

# Texto vermelho
print(colorama.Fore.RED + "\nVermelho" + colorama.Style.RESET_ALL)
# Letra pequena, normal e grande
print(colorama.Style.DIM + "Diminuir" + colorama.Style.RESET_ALL)
print(colorama.Style.NORMAL + "Normal" + colorama.Style.RESET_ALL)
print(colorama.Style.BRIGHT + "Claridade" + colorama.Style.RESET_ALL)
# Fundo vermelho 
print(colorama.Back.RED + "Fundo Vermelho" + colorama.Style.RESET_ALL)

# Pulando linha, eerguntando o nome e guardando na variável name
name=input("\nQual é o seu nome ? ")
# Monstrando a mensagem mais o que tem na variável name
print(f"Bem vindo {name}")
name = "João"
print(f"O tipo de conteúdo na variável name é {type(name)}\n")

