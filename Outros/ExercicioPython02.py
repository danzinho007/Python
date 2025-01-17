print('1-Criar Script que leia o nome da pessoa e mostre uma mensagem') 
print('de Boas-Vindas de acordo com a mensagem digitada')
nome = input('Qual e o seu nome ? ')
print('Olá',nome,',seja bem-vindo !')
print('Olá {}, seja bem-vindo !'. format(nome))
print('2-Criar Script que leia o dia, o mês e o ano de nascimento e') 
print('mostr uma mensagem com a data formatada')
nasci = input('Qual dia, mês e ano você nasceu ?')
print(nasci)
print('3-Criar Script que leia dois números e tente mostrar a soma')
print('entre eles')
n1 = input('Digite o 1° número : ')
print(type(n1))
n2 = int(input('Digite o 2° número : ')) # int(input) Converte a string em número
print(type(n2))
n3 = int(input('Digite o 3° número : '))
print(type(n3))
#s1 = n1 + n2 < Erro pois o valor n1 é um string
s2 = n2 + n3
print('A soma vale ', s2) 
print('A soma entre ', n2, 'e', n3, 'vale', s2)
print('A soma entre {} e {} vale {}' .format(n2, n3, s2))
print('A soma entre {0} e {1} vale {2}' . format(n2, n3, s2))

n4 = float(input('Digite o 4° número : ')) # float(input) Converte a string pra Float ou seja, um número Real. Ex 4 ( Inteiro ) em Float é 4.0
print(4)
n5 = str(input('Digite o 5° número : ')) # str(input) Converte a string em String
n6 = bool(input('Digite o 6° número : ')) # bool(input) Converte a string em Boela ( True ou False )
print(n5)
print(type(n4))
print(type(n5))
print(type(n6))

n7 = input('Digite o 7° número para verificação : ')
# Digitando 0 para o número

print('O tipo primitivo do valor ', n7 , 'é', type(n7))

print('O número é numérico ?', n7.isnumeric())
# 0 é número ? Sim, logo True
# Retorna True se todos os caracteres da string forem numéricos e houver pelo menos um caractere . Os caracteres numéricos incluem caracteres de dígitos e todos os caracteres que possuem a propriedade de valor numérico Unicode, por exemplo, U+2155, FRAÇÃO VULGAR UM QUINTO. 

print('O número é alfa ?', n7.isalpha())
# 0 é letra ? Não, logo False
# Retorna True se todos os caracteres da string forem alfabéticos e houver pelo menos um caractere. Os caracteres alfabéticos são aqueles definidos no banco de dados de caracteres Unicode como “Letter”

print('O número é um alfa numérico ?',n7.isalnum())
# 0 é número ? Sim, logo True
# Um caractere é alfa numérico se um dos seguintes retornar True: 
# c.isalpha(), c.isdecimal(), c.isdigit() ou c.isnumeric()

print('O número está em letra maiúscula ?', n7.isupper())
# Retorne True se todos os caracteres 4 em maiúsculas na string forem maiúsculos e houver pelo menos um caractere em maiúsculas

print('O conteúdo', n7, 'tem formato ASCII ?', n7.isascii())
# Retorna True se a string estiver vazia ou todos os caracteres na string forem ASCII, Falsecaso contrário. Os caracteres ASCII têm pontos de código no intervalo U+0000-U+007F.

print('O conteúdo', n7, 'tem espaço em branco na string ?', n7.isspace())
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

print('O conteúdo0', n7, 'é uma string com títulos em maiúsculas e tem pelos menos 1 caractere ?', n7.istitle())
# Retorne True se a string for uma string com título em maiúsculas e houver pelo menos um caractere, por exemplo, caracteres maiúsculos só podem seguir caracteres não maiúsculos e caracteres minúsculos somente os maiúsculos. 

# ver aqui 
# https://docs.python.org/3/library/stdtypes.html#string-methods

