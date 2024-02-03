import requests
import json

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()['data']

    # Extrair apenas os campos desejados e classificar as cartas pelo nome
    simplified_cards = sorted(data, key=lambda x: x['name'])
    simplified_cards = [
        {'id': card['id'], 'name': card['name'], 'type': card['type'], 'desc': card['desc'], 'race': card.get('race', '')}
        for card in simplified_cards
    ]

    # Salvar as cartas simplificadas em um arquivo JSON
    with open("cartas_simplificadas.json", "w") as file:
        json.dump(simplified_cards, file, indent=2)  # indent para formatar o JSON mais legível
else:
    print(f"Erro na solicitação: {response.status_code}")
