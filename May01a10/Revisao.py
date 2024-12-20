# 1 Formatação de texto / fundo 
# 2 Imprimindo na tela algo
# 3 Entrada de dados : Guarda algo que veio de um comando numa variável e exibe na tela
# 4 Operadores Aritméticos
# 5 Operadores Comparativos
# 6 Operadores Lógicos 
# 7 Saída de dados 
# 8 Estrutura condicional
# 9 Estrutura repetitiva enquanto
# 10 Estrutura repetitiva para

import colorama
import math
colorama.init()

print("\nComentários em Python : ")
print('Exemplo 1 : # Comentário de uma linha ')
print("Exemplo 2 : ''' Comentário de várias linhas '''")
print('Exemplo 3 : """ Comentário de várias linhas """ \n')

# Texto vermelho
print(colorama.Fore.RED + "\nVermelho" + colorama.Style.RESET_ALL)
# Letra pequena, normal e grande
print(colorama.Style.DIM + "Diminuir" + colorama.Style.RESET_ALL)
print(colorama.Style.NORMAL + "Normal" + colorama.Style.RESET_ALL)
print(colorama.Style.BRIGHT + "Claridade" + colorama.Style.RESET_ALL)
# Fundo vermelho 
print(colorama.Back.RED + "Fundo Vermelho" + colorama.Style.RESET_ALL)

# Entrada de dados :
# Pulando linha, eerguntando o nome e guardando na variável name
name=input("\nQual é o seu nome ? ")
# Monstrando a mensagem mais o que tem na variável name
print(f"Bem vindo {name}")
print(f"O tipo de conteúdo na variável name é {type(name)}")
idade=int(input("\nQuantos anos você tem ? "))
print(f"{name} tem {idade} anos")
print(f"O tipo de conteúdo na variável idade é {type(idade)}")

print("\nOutros comandos : ")
print("Lista")
print("Embaralhar lista")
print("Ordenar lista")
print("Sortear lista")

print("\nOperadores matemáticos : ")
print("Adição : +")
print("Subtração : -")
print("Multiplicação : *")
print("Divisão : /")
print("Divisão inteira : //")
print("Resto da divisão : %")
print("Exponenciação : **")
print("Radiciação : number **(1/2)")
print(f"A raiz quadrada de {idade} é {math.sqrt(idade):.2f}") # Precisa da biblioteca math

print("\nOperadores comparativos")
print("Maior : >")
print("Maior ou igual : >=")
print("Menor : <")
print("Menor ou igual : <=")
print("Igual : =] ")
print("Diferente : != ou <>")

print("\nOperadores Lógicos :")
print("E : and")
print("Ou : or")
print("Não : not")

print("\nSaída de dados : ")
print("print("")")
print("Tipo int : Placeholder de formatação %d")
print("Tipo float : Placeholder de formatação %f")
print("Tipo str : Placeholder de formatação %s")

print("\nEstrutura Condicional :")
print("Simples = Se : if")
print("Composta = Se ... senão : if ... else")
print("Encadeamento = Se ... senão se ... se : if ... elif ... else")

print("\nEstrutura repetitiva : ")
print("Enquanto : while")
print("Enquanto algo for Verdadeiro, executa e volta")
print("Caso venha ser falso, pula fora")

print("\nBiblioteca math : import math")
print("Ângulo")
print("Arco")
print("Arredondamento")
print("Exponencial")
print("Fatorial")
print("Funções hiperbólicas")
print("Funções trigonométricas")
print("Hipotenusa")
print("Logaritmo")
print("Pi")
print("Potência")
print("Raiz quadrada")
print("Truncamento")

print("\nBiblioteca random : imprt random")
print("Escolher algo de uma lista")
print("Simular carca ou coroa")
print("Lançar dado")
print("Sortear número")
print("Sortear 3 pessoas")
print("Embaralhar uma lista")
print("Geral número decimal")

print("Biblioteca random com string : ")
print("Gerar senha aleatória")
