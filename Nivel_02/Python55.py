def soma (a, b):
    return(a + b)
a = 5
b = 5
print(soma(4, 3))

# Explicação : 

def soma (a, b):
# def = Palavra-chave reservada que define função
# Função soma recebendo 2 argumentos : a e b 
    return (a + b)
# Retornando a soma entre os 2 argumentos : a e b

a = 5
b = 5
# Atribuíndo valores 5 e 5 nas variáveis a e b

print(soma(4,3))
# Quando chama a função soma, você passa os valores definidos antes na função, não os valores nas variáveis

# ////////////////////////////////////////////// #

resultado = soma(a, b)
# Atribui a soma de a  e b para variável resultado

print(resultado)
# Isso imprimirá "10" no console, que é a soma de 5 e 5

print(soma(a, b))
# Imprime o resultado da soma de a e b diretamente na tela  que é 10

# Quando atribui valores, ele soma, por isso : print(soma(4,3)) é 7
# Quando atribui variáveis, ele soma o conteúdo das variáveis, por isso : print(soma(a, b)) é 10

def soma (a, b):
    return(a + b)
a = 'a'
b = 'b'
# a e b atribuídas como strings ( sequência de caracteres, são colocadas em apas ou aspas duplas, são imutáveis ) as variáveis a e b
print(soma(a, b))
# Imprime ab 

# ////////////////////////////////////////////// #

# 4 = 5
# 3 = 5
# Erro :Expression cannot be assignment target
# Em Python, as variáveis não podem ter nomes numéricos, elas devem começar com uma letra ou um sublinhado.

print(soma(4,3))
# Imprime : Syntax Error cannot assign to literal here. 

# ////////////////////////////////////////////// #

def soma(a, b):
    return (c + d)
a = 5
b = 5
c = 4
d = 4
print(soma(4, 3))
# Imprime 8 que é o resultado de c + d
print(a, b, c, d)
# Imprime 5 5 4 4 

# ////////////////////////////////////////////// #

def soma(a, b):
    return (c + d)
    return (e + f)
a = 5
b = 5
c = 4
d = 4
e = 3
f = 3
print(soma(4, 3))
# Imprime 8 pois o 2° return é ignorado

# ////////////////////////////////////////////// #

def soma(a, b):
    if a == 4 and b == 3:
        return (c + d)
    else:
        return (e + f)
# A função soma verifica se a é igual a 4 e b é igual a 3. Se essa condição for verdadeira, o primeiro return será executado e o resultado da soma de c e d será retornado. Caso contrário, o segundo return será executado e o resultado da soma de e e f será retornado.

a = 5
b = 5
c = 4
d = 4
e = 3
f = 3
print("Como a = 4 e b = 3, logo ", soma(4, 3))
# Imprime 8
print(soma(4, 2))
# Imprime 6
