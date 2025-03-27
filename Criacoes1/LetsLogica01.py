import requests
from bs4 import BeautifulSoup

# URL da página do mapa
url = "https://www.letslogic.com/level/17837"

# Enviar uma solicitação GET para a página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Criar o objeto BeautifulSoup para fazer o parsing do HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar todos os valores dentro das tags <span class="val">
    span_vals = soup.find_all('span', class_='val')

    # Imprimir os valores encontrados
    if span_vals:
        for i, span in enumerate(span_vals, 1):
            print(f"Valor {i}: {span.text.strip()}")
    else:
        print("Nenhum valor encontrado dentro das tags <span class='val'>.")
else:
    print(f"Erro ao acessar a página. Código HTTP: {response.status_code}")
