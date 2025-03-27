def create_obk_file(file_name):
    # Conteúdo do cabeçalho
    header = bytearray([0x42, 0x4F, 0x4F, 0x21, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC8, 0xD0])
    
    # Escrever o arquivo .obk
    with open(file_name, 'wb') as f:
        f.write(header)

# Exemplo de uso
if __name__ == "__main__":
    create_obk_file("example.obk")
