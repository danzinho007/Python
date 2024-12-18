print("\nMostrar o tipo do conteúdo: \n")

inteiro = -5
decimal = 5.55
string = "Daniel"
logico1 = True
logico2 = False
valor_nulo = None

print("Tipos primitivos: 5 ")
print(f'O número -5 é: {type(inteiro)}')   
print(f'O número 5.5 é: {type(decimal)}')
print(f'A palavra "Daniel" é: {type(string)}')
print(f'O valor True é: {type(logico1)}')
print(f'O valor False é: {type(logico2)}')
print(f'O valor None é: {type(valor_nulo)}')

print("\nTipos compostos: 4 ")
lista = [1, 2, 3, 4]       # list
tupla = (1, 2, 3)          # tuple
conjunto = {1, 2, 3}       # set
dicionario = {"nome": "Maria", "idade": 30}  # dict
print(f'A lista [1, 2, 3, 4] é: {type(lista)}')
print(f'A tupla (1, 2, 3) é: {type(tupla)}')
print(f'O conjunto {1, 2, 3} é: {type(conjunto)}')
print(f'O dicionário {dicionario} é: {type(dicionario)}')

print("\nOutros tipos: 3") 
bytes_data = b'hello'      # bytes
bytearray_data = bytearray([65, 66, 67])  # bytearray
conjunto_congelado = frozenset([1, 2, 3])  # frozenset

print(f'O valor b"hello" é: {type(bytes_data)}')
print(f'O valor bytearray([65, 66, 67]) é: {type(bytearray_data)}')
print(f'O conjunto frozenset([1, 2, 3]) é: {type(conjunto_congelado)}\n')

'''
Resumo :

Tipos Primitivos (Básicos) :
int: Números inteiros. Exemplo: a = 10
float: Números de ponto flutuante (reais). Exemplo: b = 3.14
str: Sequência de caracteres (strings). Exemplo: s = "Python"
bool: Valores lógicos (True ou False). Exemplo: flag = True
NoneType: Representa a ausência de valor. Exemplo: x = None

Tipos Compostos (Coleções) :
list: Lista ordenada e mutável. Exemplo: l = [1, 2, 3]
tuple: Tupla ordenada e imutável. Exemplo: t = (1, 2, 3)
set: Conjunto não ordenado de itens únicos. Exemplo: s = {1, 2, 3}
dict: Dicionário (pares chave-valor). Exemplo: d = {'nome': 'Maria', 'idade': 30}

Outros Tipos Importantes
bytes: Sequência imutável de bytes. Exemplo: b = b'hello'
bytearray: Sequência mutável de bytes. Exemplo: ba = bytearray([65, 66, 67])
frozenset: Conjunto imutável. Exemplo: fs = frozenset([1, 2, 3])
range: Representa uma sequência de números, muito usado em loops. Exemplo: r = range(5)

Tipos de Funções e Objetos :
function: Funções definidas pelo usuário ou funções incorporadas. Exemplo: def minha_func(): pass
lambda: Funções anônimas (lambda functions). Exemplo: f = lambda x: x + 1

Tipos Especiais :
complex: Números complexos (com partes real e imaginária). Exemplo: z = 1 + 2j
object: A classe base de todos os objetos em Python. Tudo em Python é um objeto, então o tipo object é a base para qualquer outro tipo de dado.
type: Representa o tipo de qualquer objeto. Exemplo: t = type(10)

Tipos em Bibliotecas e Pacotes :
datetime: Para manipulação de datas e horários. Exemplo: from datetime import datetime; d = datetime.now()
Decimal: Usado para representar números decimais de precisão mais alta. Exemplo: from decimal import Decimal; d = Decimal('0.1')

Tipos de Arquivo e Entrada/Saída :
file: Representa objetos de arquivo. Exemplo: f = open('arquivo.txt', 'r')
io.BytesIO, io.StringIO: Tipos de buffer de memória para ler e escrever dados.

Tipos de Anotações (Introduzidos em Python 3.5+) :
typing: Para anotações de tipos (para tipagem estática). Exemplo: from typing import List; def foo(a: List[int]) -> int: pass

Tipo Genérico :
Any: Tipo que aceita qualquer tipo de dado, usado nas anotações de tipos. Exemplo: def func(a: Any) -> Any: pass

Tipos de Exceções :
Python também tem tipos especiais relacionados a exceções, como ValueError, IndexError, KeyError, entre outros.
'''
