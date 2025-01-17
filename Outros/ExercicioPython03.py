n7 = input('Digite algo para verificação : ')
# Digitando 0 para o número

print('O tipo primitivo do valor ', n7 , 'é', type(n7))

print('O número é um número ?', n7.isnumeric())
# 0 é número ? Sim, logo True
# Retorna True se todos os caracteres da string forem numéricos e houver pelo menos um caractere . Os caracteres numéricos incluem caracteres de dígitos e todos os caracteres que possuem a propriedade de valor numérico Unicode, por exemplo, U+2155, FRAÇÃO VULGAR UM QUINTO. 

print('O número é alfabético ?', n7.isalpha())
# 0 é letra ? Não, logo False
# Retorna True se todos os caracteres da string forem alfabéticos e houver pelo menos um caractere. Os caracteres alfabéticos são aqueles definidos no banco de dados de caracteres Unicode como “Letter”

print('O número é um alfanumérico ?',n7.isalnum())
# 0 é número ? Sim, logo True
# Um caractere é alfa numérico se um dos seguintes retornar True: 
# c.isalpha(), c.isdecimal(), c.isdigit() ou c.isnumeric()

print('Está em letra maiúscula ?', n7.isupper())
# Retorne True se todos os caracteres 4 em maiúsculas na string forem maiúsculos e houver pelo menos um caractere em maiúsculas

print('O conteúdo', n7, 'tem formato ASCII ?', n7.isascii())
# Retorna True se a string estiver vazia ou todos os caracteres na string forem ASCII, Falsecaso contrário. Os caracteres ASCII têm pontos de código no intervalo U+0000-U+007F.

print('O conteúdo', n7, 'tem espaço em branco na string e um caractere ?', n7.isspace())
# Retorna True se houver apenas caracteres de espaço em branco na string e houver pelo menos um caractere

print('O conteúdo0', n7, 'é decimal ?', n7.isdecimal())
# Retorna True se todos os caracteres da string forem decimais e houver pelo menos um caractere.

print('O conteúdo0', n7, 'é imprimível ?', n7.isprintable())
# Retorna True se todos os caracteres na string são imprimíveis ou a string está vazia .

print('O conteúdo0', n7, 'é um identificado válido ?', n7.isidentifier())
# Retorna True se a string for um identificador válido de acordo com a definição da linguagem, seção Identificadores e palavras-chave .

print('O conteúdo0', n7, 'é um dígito ?', n7.isdigit())
# Retorna True se todos os caracteres da string forem dígitos e houver pelo menos um caractere

print('O conteúdo0', n7, 'apresenta 4 caracteres em maiúscula e 1 em minúscula ?', n7.islower())
# Retorna True se todos os caracteres 4 em maiúsculas na string forem minúsculos e houver pelo menos um caractere em maiúsculas

print('O conteúdo0', n7, 'é uma string com título em maiúscula e tem pelos menos 1 caractere ?', n7.istitle())
# Retorne True se a string for uma string com título em maiúsculas e houver pelo menos um caractere, por exemplo, caracteres maiúsculos só podem seguir caracteres não maiúsculos e caracteres minúsculos somente os maiúsculos. 

# ver aqui 
# https://docs.python.org/3/library/stdtypes.html#string-methods
