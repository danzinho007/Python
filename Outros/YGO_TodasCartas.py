import requests
import json

def obter_todas_cartas():
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Erro na solicitação: {response.status_code}")
        return None

def extrair_informacoes_cartas(cartas):
    informacoes_cartas = []

    for carta in cartas:
        info_carta = {
            'id': carta['id'],
            'nome': carta['name'],
            'tipo': carta['type'],
            'descricao': carta['desc'],
            'atk': carta.get('atk', None),
            'def': carta.get('def', None),
            'level': carta.get('level', None),
            'raca': carta['race'],
            'atributo': carta.get('attribute', None),
            'conjuntos_cartas': carta.get('card_sets', None)
        }
        informacoes_cartas.append(info_carta)

    return informacoes_cartas

# Obtém todas as cartas da API
todas_cartas = obter_todas_cartas()

if todas_cartas:
    # Extrai as informações específicas de cada carta
    informacoes_cartas = extrair_informacoes_cartas(todas_cartas)

    # Salvar as informações em um arquivo JSON
    with open("todas_cartas.json", "w") as file:
        json.dump(informacoes_cartas, file, indent=2)  # indent para formatar o JSON mais legível
    print("Lista de todas as cartas salva com sucesso.")
else:
    print("Não foi possível obter as cartas.")
