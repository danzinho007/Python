import requests

# Substitua 'Dark Magician' pelo nome da carta que você deseja pesquisar
card_name = 'Dark Magician'
url = f'https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card_name}'

try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica se houve algum erro na solicitação HTTP

    data = response.json()

    # Exibindo informações sobre a carta
    if 'data' in data and data['data']:
        card_info = data['data'][0]
        print(f"Nome: {card_info['name']}")
        print(f"Atributo: {card_info['attribute']}")
        print(f"Nível: {card_info['level']}")
        print(f"Tipo: {card_info['type']}")
        print(f"Descrição: {card_info['desc']}")
    else:
        print(f"Carta '{card_name}' não encontrada.")
except requests.exceptions.HTTPError as errh:
    print(f"Erro HTTP: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Erro de Conexão: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Erro de Tempo de Requisição: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Erro durante a solicitação: {err}")
except ValueError as ve:
    print(f"Erro ao decodificar JSON: {ve}")
