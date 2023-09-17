#Quiz Python 

#Qual é o valor de frase após a execução do código ?

frase = "Python é "
frase += "incrível!"

print (frase)

# O código começa com a string "Python é " atribuída à variável frase. Em seguida, a operação += é usada para concatenar a string "incrível!" à variável frase, resultando na string completa "Python é incrível!". Finalmente, essa string é impressa usando print(frase).
# Python é incrível!

# Além desse operador, temos :
# Subtração : -=
# Multiplicação : *=
# Divisão : /=
# Exponenciação : **=
# Divisão Inteira : //= 
# Módulo : %= 

# Operadores usados em strings :

# Concatenação : +
# Junta 2 strings
string1 = "Olá, "
string2 = "mundo!"
resultado = string1 + string2
print(resultado)  # Isso imprimirá "Olá, mundo!"

# Fatiamento : [:]
# Obter uma parte específico de uma string
texto = "Python"
parte = texto[1:4]  # Obtém os caracteres da posição 1 à 3 (exclusivo), que é "yth"

# Find : ()
# Procura uma substring dentro de uma string
texto = "Python é uma linguagem de programação."
indice = texto.find("linguagem")  # Encontra a posição da palavra "linguagem"

# Indexação : []
# Acessar caracters individuais em uma string
texto = "Python"
primeiro_caractere = texto[0]  # Obtém o primeiro caractere, que é "P"

# Repetição : *
# Repetir uma string várias vezes
string = "abc"
repetida = string * 3
print(repetida)  # Isso imprimirá "abcabcabc"

# Replace ()
# Substitui todas ocorrências de uma substring por outra substring em uma string
frase = "Python é incrível!"
nova_frase = frase.replace("incrível", "fantástico")

# Split : ()
# Divide uma string em substrings com base em um delimitador e retorna uma lista das substrings
frase = "Python é incrível!"
palavras = frase.split(" ")  # Divide a frase em palavras usando espaço como delimitador

# Strip : ()
# Remove espaços em branco do início e do final de uma string
texto = "   Python   "
texto_limpo = texto.strip()  # Remove os espaços em branco
