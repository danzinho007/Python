print("\nDivisão normal")
dividendo = input('\nDigite um número: ')
divisor = int(input('Digite o divisor: '))
resultado_real = int(dividendo) // divisor
print(f'O resultado de {dividendo} por {divisor} é {resultado_real}')

print("\nDivisão diferenciada")
print(f'O número {dividendo} tem {len(dividendo)} dígito(s)')

resultado_final = ""
numero_atual = ""

for i in range(len(dividendo)):
    numero_atual += dividendo[i]
    valor = int(numero_atual)

    if valor < divisor:
        # Só adiciona 0 se já houver algum número no resultado (ignora zeros à esquerda)
        if resultado_final != "":
            resultado_final += "0"
            print(f'{valor} não é divisível por {divisor} → adiciona 0 no resultado')
    else:
        quociente = valor // divisor
        resultado_final += str(quociente)
        print(f'{valor} é divisível por {divisor} → forma {quociente} no resultado')
        resto = valor % divisor
        numero_atual = str(resto)  # reinicia com o resto
print(f'Resultado final é {resultado_final}')
print('\n')

# Exemplo 6 dividido por 2
# Verificar quantos digitos o número tem
# 1 digito
# Verificar o dividendo pelo dividor e formar grupos
# 6 forma 3 grupos de 2
# Resposta 6 dividido por 2 é 3
