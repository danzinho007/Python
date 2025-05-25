import os
import shutil

# Caminho da pasta com os arquivos
pasta_origem = r'C:\Users\Daniel\Documents\PC-  Notas\YGO-EDOPro\pics'

# Caminho onde as subpastas serão criadas
pasta_destino = r'C:\Users\Daniel\Downloads\aqui1'

# Garante que a pasta de destino exista
os.makedirs(pasta_destino, exist_ok=True)

# Lista todos os arquivos na pasta de origem
arquivos = [f for f in os.listdir(pasta_origem) if os.path.isfile(os.path.join(pasta_origem, f))]

# Quantos arquivos por pasta
tamanho_lote = 300

# Loop para dividir os arquivos
for i in range(0, len(arquivos), tamanho_lote):
    # Nome da subpasta, exemplo: "lote_1", "lote_2", etc.
    nome_subpasta = f'lote_{i // tamanho_lote + 1}'
    caminho_subpasta = os.path.join(pasta_destino, nome_subpasta)
    os.makedirs(caminho_subpasta, exist_ok=True)

    # Move os arquivos para a subpasta
    for arquivo in arquivos[i:i + tamanho_lote]:
        origem = os.path.join(pasta_origem, arquivo)
        destino = os.path.join(caminho_subpasta, arquivo)
        shutil.move(origem, destino)

print("Arquivos organizados em lotes!")
