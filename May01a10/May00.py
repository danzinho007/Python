import colorama
# Inicializa a biblioteca colorama
colorama.init()
# Exibe texto em diferentes cores
print(colorama.Fore.RED + "\nVermelho")
print(colorama.Fore.GREEN + "Verde")
print(colorama.Fore.YELLOW + "Amarelo")
print(colorama.Fore.BLUE + "Azul")
print(colorama.Fore.MAGENTA + "Magenta")
print(colorama.Fore.CYAN + "Ciano")
print(colorama.Fore.WHITE + "Branco")
print(colorama.Fore.RESET)

# Exibe texto em diferentes estilos
print(colorama.Style.DIM + "Diminuir" + colorama.Style.RESET_ALL)
print(colorama.Style.NORMAL + "Normal" + colorama.Style.RESET_ALL)
print(colorama.Style.BRIGHT + "Claridade" + colorama.Style.RESET_ALL)
print(colorama.Style.RESET_ALL)

# Exibe texto em diferentes fundos
print(colorama.Back.BLACK + "Fundo Preto" + colorama.Style.RESET_ALL)
print(colorama.Back.RED + "Fundo Vermelho" + colorama.Style.RESET_ALL)
print(colorama.Back.GREEN + "Fundo Verde" + colorama.Style.RESET_ALL)
print(colorama.Back.YELLOW + "Fundo Amarelo" + colorama.Style.RESET_ALL)
print(colorama.Back.BLUE + "Fundo Azul" + colorama.Style.RESET_ALL)
print(colorama.Back.MAGENTA + "Fundo Magenta" + colorama.Style.RESET_ALL)
print(colorama.Back.CYAN + "Fundo Ciano" + colorama.Style.RESET_ALL)
print(colorama.Back.WHITE + "Fundo Branco" + colorama.Style.RESET_ALL)
print(colorama.Back.RESET)

# Exibe texto com combinação de cores e fundos
print(colorama.Fore.RED + colorama.Back.GREEN + colorama.Style.BRIGHT + "Olá Mundo" + colorama.Style.RESET_ALL)

# Exibe texto com reset
print(colorama.Fore.GREEN + "Texto verde" + colorama.Style.RESET_ALL + " e texto normal\n")
