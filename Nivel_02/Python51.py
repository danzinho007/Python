# Executar com F5

# def saudacao(nome):
#     print(f"Olá, {nome}!")
# saudacao("João", "Futi")

def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao("João")

# Resumindo : Ele criou uma função com nome de saudacao que tem conteúdo nome + print com f-string, depois ele chama essa funcão e atribui valor a ela

# def é uma palavra-chave usada em Python para definir uma função. Em def saudacao(nome):, estamos definindo uma função chamada saudacao que recebe um parâmetro nome.

# A sintaxe f"..." é usada em Python para criar strings formatadas, também conhecidas como f-strings. As f-strings permitem inserir valores de variáveis ​​diretamente em uma string, tornando a concatenação de strings e variáveis ​​mais fácil e legível.

# Ao usar uma f-string, os valores de variáveis ​​são colocados dentro de chaves {} dentro da string. Por exemplo, em f"Olá, {nome}!", o valor da variável nome será inserido na string. O f antes da aspas duplas indica que é uma f-string.

# O ! dentro dos colchetes {} é um operador de formatação que permite aplicar um método específico de formatação à variável inserida na string. Por exemplo, em f"Olá, {nome.upper()}!", o método upper() será aplicado à variável nome, convertendo todas as letras em maiúsculas antes de inserir na string.

# Outros operadores de formatação incluem :d para números inteiros, :.2f para números de ponto flutuante com duas casas decimais, entre outros. A sintaxe completa das f-strings é bem flexível e pode ser personalizada para atender às necessidades específicas de formatação de strings.