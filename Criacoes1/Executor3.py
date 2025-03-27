def executa_codigo(codigo):
    estado_variaveis = {}
    exec(codigo, globals(), estado_variaveis)
    a = estado_variaveis.get('a', 0)
    while a < 10:
        print(f"Variable a = {a} / Output = {a}")
        a += 2
    print(f"Variable a = {a}")
    if a > 10:
        print("Resultado final = 9")
codigo_exemplo = """
a = 1
"""
executa_codigo(codigo_exemplo)