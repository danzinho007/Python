def executa_codigo(codigo):
    # Dicionário para armazenar o estado das variáveis
    estado_variaveis = {}

    # Execute o código passado como parâmetro
    exec(codigo, globals(), estado_variaveis)

    # Exiba o estado final das variáveis
    print("Estado final das variáveis:")
    for var, val in estado_variaveis.items():
        print(f"{var}: {val}")

# Código de exemplo
codigo_exemplo = """
a = 1
while a < 10:
    print (a)
    a+=2
"""

# Executar o código de exemplo
executa_codigo(codigo_exemplo)
