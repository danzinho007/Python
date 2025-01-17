import requests
import random

def obter_todas_cartas():
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Erro na solicitação: {response.status_code}")
        return None

def gerar_deck_aleatorio(cartas, tamanho_do_deck=40):
    # Embaralhar todas as cartas
    random.shuffle(cartas)

    # Selecionar um subconjunto para formar o deck
    deck = cartas[:tamanho_do_deck]

    return deck

# Obtém todas as cartas da API
todas_cartas = obter_todas_cartas()

if todas_cartas:
    # Gera um deck aleatório
    deck_aleatorio = gerar_deck_aleatorio(todas_cartas, tamanho_do_deck=40)

    # Exibe as informações do deck gerado
    for carta in deck_aleatorio:
        print(f"ID: {carta['id']}, Nome: {carta['name']}, Tipo: {carta['type']}")
else:
    print("Não foi possível obter as cartas.")
