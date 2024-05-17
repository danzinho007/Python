def executa_codigo(codigo):
    # Dicionário para armazenar o estado das variáveis
    estado_variaveis = {}

    # Execute o código passado como parâmetro
    exec(codigo, globals(), estado_variaveis)

    # Inicializa a variável a com o valor inicial
    a = estado_variaveis.get('a', 0)

    # Loop while
    while a < 10:
        # Exibe o valor da variável a
        print(f"Variable a = {a} / Output = {a}")
        # Atualiza o valor de a
        a += 2

    # Exibe o valor de a após a conclusão do loop
    print(f"Variable a = {a}")

    # Se a for maior que 10, exibe o resultado final como 9
    if a > 10:
        print("Resultado final = 9")

# Código de exemplo
codigo_exemplo = """
a = 1
"""

# Executar o código de exemplo
executa_codigo(codigo_exemplo)
