# Quiz Python

# Qual variável contém o valor "3" após a execução do código ?

x = 2
y = 3
z = 4

x = y
# x se torna 3 ( veio de y )
y = z
# y se torna 4 ( veio de z )
z = x
# z se torna 3 ( veio de x )

print(x, y, z)
# Resposta C ) Nenhum

"""LEMBRANDO : CUIDADO com as formas resumidas !!!
Chamadas de Operações de Atribuição aumentada 

Em Python, existem várias operações de atribuição aumentada (também chamadas de operações de atribuição composta) que permitem realizar operações aritméticas e atribuição em uma única expressão. Aqui estão algumas delas:

x += y: Isso adiciona o valor de y a x e atribui o resultado a x. É equivalente a x = x + y.

x -= y: Isso subtrai o valor de y de x e atribui o resultado a x. É equivalente a x = x - y.

x *= y: Isso multiplica x pelo valor de y e atribui o resultado a x. É equivalente a x = x * y.

x /= y: Isso divide x pelo valor de y e atribui o resultado a x. É equivalente a x = x / y.

x //= y: Isso realiza uma divisão inteira de x por y e atribui o resultado a x. É equivalente a x = x // y.

x %= y: Isso calcula o resto da divisão de x por y e atribui o resultado a x. É equivalente a x = x % y.

x *= y: Isso eleva x à potência de y e atribui o resultado a x. É equivalente a x = x * y.

Essas operações de atribuição aumentada são úteis para simplificar o código e realizar operações aritméticas e de atribuição de forma concisa.

LEMBRANDO TB !!! 

Em Python não tem como juntar o conteúdo que seja número de uma variável com outra e formar um novo número 
Ex : x = 2 e y = 3, não tem como mostrar 23
 
A pessoa precisa formatar os valores em string
x = 2    y = 3
resultado = str(x) + str(y)
print(resultado)  # Isso imprimirá "23"""
