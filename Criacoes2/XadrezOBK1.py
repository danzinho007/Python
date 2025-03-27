# Movimento 1.e4 e5

# Explicando :  42 4F 4F 21 
#               02 00 00 00 
#               04 00 00 00 
#               4C DC F4 E4
#               44 D0
# Resumindo : 
# 1- Identifica o arquivo como obk do Chessmaster
# 2- Número de movimentos estão no arquivo
# 3- Tamanho dos Textos / Notas
# 4- Movimentos 
         
# 42 4F 4F 21 Cabeçalho do arquivo .obk

# 02 00 00 00 Número total de movimentos, se lê de trás pra frente
# Exemplo 6E 59 04 00 é 0x00459E6 em Hexadecimal, o que á 285.038 em decimal
# 04 00 00 00 Tamanho total dos textos e notas em Little-Endia

# 4C DC F4 E4 : Movimento 1.e4
# 4C e E4 são coordenadas da casa e4
# DC e F4 são bytes que representam o número do movimento 1 em Little-Endian

# 44 DO : Peso do movimento 1.e4
# D0 é o peso de 1.e4 que representa 100 em decimal

# 00 00 00 00 : Representa e5
# Todos os bytes são 0, indicando que não há movimento específico para o segundo movimento.

# 42 4F 4F 21 = Cabeçalho
# 04 00 00 00 = 4 movimentos
# 06 00 00 00 = 6 bytes de texto 
# 4C DC 74 E4 = 1.e4
# 48 D0 F0 E8 = 1.e5
# 00 00 00 00 = 2.a3
# 00 00       = 2.a6 

header = bytearray([0x42, 0x4F, 0x4F, 0x21])  # Cabeçalho BOO!
moves = bytearray([
    0x02, 0x00, 0x00, 0x00,  # Número de movimentos (2 movimentos)
    0x00, 0x00, 0x00, 0x00,  # Tamanho dos textos/notas (0 bytes)
    0x4C, 0xDC, 0xF4, 0xE4,  # Movimento 1: 1.e4
    0x00, 0x00, 0x00, 0x00,
    0xC8, 0xD0               # Movimento 2: 2.a3
])

# Escrevendo o arquivo
with open('example.obk', 'wb') as file:
    file.write(header + moves)
