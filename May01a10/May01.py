# 1
print('\n\033(1;32;40m Olá Mundo\033[m')
# 2
print("\033[1;32;40m Olá Mundo\033[m")

# Sobre 1 e 2 :
# O ambiente onde você está executando o código não suporta ANSI escape sequences. Isso pode acontecer se você estiver executando o código em um ambiente que não é um terminal, como um IDE ou um ambiente de desenvolvimento online.

from colorama import init, Fore, Back, Style
# Importando funções init, Fore, Back e Style da biblioteca colorama. A colorama é uma biblioteca que permite imprimir texto colorido no terminal, mesmo em ambientes que não suportam ANSI escape sequences.

init()
# Inicializando a biblioteca colorama. Isso é necessário para que as funções de impressão de texto colorido funcionem corretamente.

print(f"{Fore.GREEN}Olá Mundo{Style.RESET_ALL}")
print(f"{Back.RED}{Fore.GREEN}Olá Mundo{Style.RESET_ALL}")
print(f"{Back.RED}{Fore.GREEN}{Style.BRIGHT}Olá Mundo{Style.RESET_ALL}\n")
# - f-string é usado para formatação de string. Ele permite inserir expressões python dentro de strings.

# - Fore.GREEN é uma constante da biblioteca colorama que representa a cor verde.

# - Style.RESET_ALL é outra constante da biblioteca colorama que reseta a cor do texto para a cor padrão do terminal.

"""
Cores:
- Fore.BLACK
- Fore.RED
- Fore.GREEN
- Fore.YELLOW
- Fore.BLUE
- Fore.MAGENTA
- Fore.CYAN
- Fore.WHITE
- Fore.LIGHTBLACK_EX
- Fore.LIGHTRED_EX
- Fore.LIGHTGREEN_EX
- Fore.LIGHTYELLOW_EX
- Fore.LIGHTBLUE_EX
- Fore.LIGHTMAGENTA_EX
- Fore.LIGHTCYAN_EX
- Fore.LIGHTWHITE_EX

Estilos:
- Style.DIM
- Style.NORMAL
- Style.BRIGHT
- Style.RESET_ALL

Fundos:
- Back.BLACK
- Back.RED
- Back.GREEN
- Back.YELLOW
- Back.BLUE
- Back.MAGENTA
- Back.CYAN
- Back.WHITE
- Back.LIGHTBLACK_EX
- Back.LIGHTRED_EX
- Back.LIGHTGREEN_EX
- Back.LIGHTYELLOW_EX
- Back.LIGHTBLUE_EX
- Back.LIGHTMAGENTA_EX
- Back.LIGHTCYAN_EX
- Back.LIGHTWHITE_EX

"""
