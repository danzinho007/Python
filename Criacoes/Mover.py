import os
import random
import shutil

# Caminho da pasta que contém as imagens
caminho_origem = r"C:\Users\Daniel\Pictures\Nomear"

# Caminho onde as novas pastas serão criadas
caminho_destino = r"C:\Users\Daniel\Destino"  # Ajuste para o caminho desejado

# Número de arquivos por pasta
arquivos_por_pasta = 10

# Lista de todos os arquivos na pasta
arquivos = [f for f in os.listdir(caminho_origem) if f.endswith('.jpg')]

# Embaralhar os arquivos para obter uma seleção aleatória
random.shuffle(arquivos)

# Contador de pastas
contador_pasta = 1

# Lista para armazenar os nomes das pastas criadas
pastas_criadas = []

# Loop para criar pastas e mover arquivos
while arquivos:
    # Nome da nova pasta
    nome_pasta = f"pasta_{contador_pasta:02d}"
    caminho_pasta = os.path.join(caminho_destino, nome_pasta)  # Usa caminho_destino para criar as pastas

    # Criar a pasta se não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
        print(f"Pasta criada: {caminho_pasta}")
    else:
        print(f"Pasta já existe: {caminho_pasta}")

    # Adicionar o nome da pasta à lista de pastas criadas
    pastas_criadas.append(caminho_pasta)  # Adiciona o nome mesmo se a pasta já existir

    # Selecionar 10 arquivos ou menos (se não houver mais 10 arquivos)
    arquivos_para_mover = arquivos[:arquivos_por_pasta]
    arquivos = arquivos[arquivos_por_pasta:]

    # Mover os arquivos para a nova pasta
    for arquivo in arquivos_para_mover:
        origem = os.path.join(caminho_origem, arquivo)
        destino = os.path.join(caminho_pasta, arquivo)
        try:
            shutil.move(origem, destino)
            print(f"Arquivo {arquivo} movido para {caminho_pasta}")
        except Exception as e:
            print(f"Erro ao mover {arquivo}: {e}")

    # Incrementar o contador de pastas
    contador_pasta += 1

# Verificar e imprimir os nomes das pastas criadas
if pastas_criadas:
    print("\nPastas criadas:")
    for pasta in pastas_criadas:
        print(pasta)
else:
    print("Nenhuma pasta foi criada.")

print("Arquivos movidos com sucesso!")
