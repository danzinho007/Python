from PIL import Image
import os

# Caminho para a pasta com as imagens .webp
input_folder = r"C:\Users\Daniel\Downloads"  # Use o prefixo "r" antes do caminho
output_folder = r"C:\Users\Daniel\Downloads"  # Use o prefixo "r" antes do caminho

# Cria a pasta de saída, se ela não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop pelas imagens na pasta
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".webp"):  # Verifica se o arquivo é .webp
        input_path = os.path.join(input_folder, filename)
        
        # Abre a imagem
        with Image.open(input_path) as img:
            # Gira a imagem 90° no sentido anti-horário
            rotated_img = img.rotate(90, expand=True)
            
            # Obtém as dimensões da imagem
            width, height = rotated_img.size
            
            # Calcula o novo tamanho (dobro)
            new_size = (width * 2, height * 2)
            
            # Redimensiona a imagem
            resized_img = rotated_img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Define o caminho para salvar a imagem convertida em .jpg
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_filename)
            
            # Salva a imagem como .jpg
            resized_img = resized_img.convert("RGB")  # Converte para RGB, necessário para salvar como JPG
            resized_img.save(output_path, "JPEG")
            print(f"Imagem salva: {output_path} com tamanho {new_size}")

print("Processo concluído!")
