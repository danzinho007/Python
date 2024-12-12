print("Write a program that reads something from the keyboard and shows its primitive type and all the possible information about him")
value = input('Type something: ')
print('The primitive type of this value is:', type(value))

print('\nIs a number ?', value.isalnum())
print('Is alphabetical ?', value.isalpha())
print('Does the value ', value, 'have ASCII format ?', value.isascii())

print('\nThe value', value, 'is decimal?', value.isdecimal())
print('The value', value, 'is a digit?', value.isdigit())
print('The value', value, 'is a valid identifier?', value.isidentifier())

print('\nis lower?', value.islower())
print('The content', value, 'is a number? ', value.isnumeric())
print('Is the value', value, 'printable?', value.isprintable())

print('\nThere are only spaces?', value.isspace())
print('Is the value' , value, 'is a string with titles in uppercase and has at least 1 character ?', value.istitle())
print('Is upper ?', value.isupper())

# Explicando os 12 :

# isalnum ? OK 1
# 0 é número ? Sim, logo True
# Um caractere é alfa numérico se um dos seguintes retornar True: 
# c.isalpha(), c.isdecimal(), c.isdigit() ou c.isnumeric()

# isalpha ? OK 2
# 0 é letra ? Não, logo False
# Retorna True se todos os caracteres da string forem alfabéticos e houver pelo menos um caractere. Os caracteres alfabéticos são aqueles definidos no banco de dados de caracteres Unicode como “Letter”

# isascii ? OK 3
# Retorna True se a string estiver vazia ou todos os caracteres na string forem ASCII, Falsecaso contrário. Os caracteres ASCII têm pontos de código no intervalo U+0000-U+007F.

# isdecimal ? OK 4
# Retorna True se todos os caracteres da string forem decimais e houver pelo menos um caractere.

# isdigit ? OK 5
# Retorna True se todos os caracteres da string forem dígitos e houver pelo menos um caractere

# isidentifier ? OK 6
# Retorna True se a string for um identificador válido de acordo com a definição da linguagem, seção Identificadores e palavras-chave .

# islower ? OK 7
# Retorna True se todos os caracteres 4 em maiúsculas na string forem minúsculos e houver pelo menos um caractere em maiúsculas

# isnumeric ? OK 8
# 0 é número ? Sim, logo True
# Retorna True se todos os caracteres da string forem numéricos e houver pelo menos um caractere . Os caracteres numéricos incluem caracteres de dígitos e todos os caracteres que possuem a propriedade de valor numérico Unicode, por exemplo, U+2155, FRAÇÃO VULGAR UM QUINTO. 

# isprintable ? OK 9
# Retorna True se todos os caracteres na string são imprimíveis ou a string está vazia .

# isspace ? OK 10
# Retorna True se houver apenas caracteres de espaço em branco na string e houver pelo menos um caractere

# istitle ? OK 11
# Retorne True se a string for uma string com título em maiúsculas e houver pelo menos um caractere, por exemplo, caracteres maiúsculos só podem seguir caracteres não maiúsculos e caracteres minúsculos somente os maiúsculos. 

# isupper ? OK 12
# Retorne True se todos os caracteres 4 em maiúsculas na string forem maiúsculos e houver pelo menos um caractere em maiúsculas

# Exemplos pra testar :

# ( Vazio ) = 2 de 12 ( ASCII e Printável )

# 0 ( zero ) = 6 de 12 ( AlfaNumérico, ASCII, Decimal, Dígito, Número e Printável )
# 8 : 6 de 12 ( AlfaNumérico, ASCII, Decimal, Dígito, Número e Printável )

# a : 6 de 12 ( AlfaNumérico, Alfabético, ASCIII, Identificador Válido, Minúsculo e Printável )
# A : 7 de 12 ( AlfaNumérico, Alfabético, ASCII, Identificador Válido, Printável, Título e Maiúsculo )

# daniel : 5 de 12 ( AlfaNumérico, Alfabético, ASCII, Identificador Válido e Printável )
# Daniel : 6 de 12 ( AlfaNumérico, Alfabético, ASCII, Identificador Válido, Printável e é um Título )
# DANIEL : 6 de 12 ( AlfaNumérico, Alfabético, ASCII, Identificador Váldo, Printável e Maiúsculo )
# Daniel7 : 5 de 12 ( AlfaNumérico, ASCII, Identificador Válido, Printável e é um Título )
# Daniel 7 : 3 de 12 ( ASCII, Printável e Título )

# Por que "Daniel" é um Título e "daniel" não é ?
# Porque "Daniel" tem pelo menos 1 caractere em maiúsculo

# Por que "Daniel7" não é alfabético ?
# Pra ser todos os caracteres da string devem ser letras e precisa de pelo menos um caractere

# Por que "DANIEL" não e´título ?
# Pra ser Título precisa que a string tenha somente letras maiúsculas ou maiúsculas seguidas de minúsculas, mínimo 1 caractere
