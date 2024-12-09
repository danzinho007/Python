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

    # Verificar se há valores suficientes para pegar o 9º valor
    if len(span_vals) >= 9:
        completed_value = span_vals[8].text.strip()  # O valor 'completed' está na 9ª posição (índice 8)
        print(f"Valor de completados para o nível 17837: {completed_value}")
    else:
        print("Não foi possível encontrar o valor de completados.")
else:
    print(f"Erro ao acessar a página. Código HTTP: {response.status_code}")
