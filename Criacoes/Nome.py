import os
import pytesseract
from PIL import Image
import re

# Especifique o caminho completo para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abra a imagem
img = Image.open('imagem.jpg')

# Extraia o texto da imagem
text = pytesseract.image_to_string(img)

# Remova espaços, quebras de linha e caracteres especiais do texto
text = re.sub(r'[^\w\s-]', '', text).replace(' ', '').replace('\n', '')

# Verifique se o arquivo original existe antes de renomear
if os.path.exists('imagem.jpg'):
    # Renomear o arquivo
    try:
        os.rename('imagem.jpg', f'{text}.jpg')
        print(f"Arquivo renomeado para {text}.jpg")
    except Exception as e:
        print(f"Erro ao renomear o arquivo: {e}")
else:
    print("O arquivo 'imagem.jpg' não foi encontrado.")
