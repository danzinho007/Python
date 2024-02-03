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

def filtrar_cartas(cartas, tipos_permitidos, tipos_excluidos):
    return [carta for carta in cartas if carta['type'] in tipos_permitidos and carta['type'] not in tipos_excluidos]

def gerar_deck_aleatorio(cartas, tamanho_main=40, tamanho_extra=15, tamanho_side=15):
    # Filtrar cartas do Extra Deck
    tipos_extra_deck = ["Fusion Monster", "Link Monster", "Pendulum Effect Fusion Monster",
                        "Synchro Monster", "Synchro Pendulum Effect Monster",
                        "Synchro Tuner Monster", "XYZ Monster", "XYZ Pendulum Effect Monster"]

    extra_deck = filtrar_cartas(cartas, tipos_extra_deck, ["Skill Card", "Token"])

    # Verificar se há pelo menos 15 cartas no Extra Deck
    if len(extra_deck) < tamanho_extra:
        print("Não há cartas suficientes no Extra Deck. Tente novamente.")
        return None, None, None

    # Filtrar cartas para o Main Deck e Side Deck
    cartas_para_deck = [carta for carta in cartas if carta not in extra_deck]
    
    # Filtrar cartas do Main Deck
    main_deck = filtrar_cartas(cartas_para_deck, ["Normal Monster", "Effect Monster"], ["Skill Card", "Token"])[:tamanho_main]

    # Filtrar cartas do Side Deck
    side_deck = filtrar_cartas(cartas_para_deck, ["Normal Monster", "Effect Monster"], ["Skill Card", "Token"])[tamanho_main:tamanho_main + tamanho_side]

    # Selecionar as 15 primeiras cartas do Extra Deck
    extra_deck = extra_deck[:tamanho_extra]

    return main_deck, extra_deck, side_deck

# Obtém todas as cartas da API
todas_cartas = obter_todas_cartas()

if todas_cartas:
    # Gera um deck aleatório
    main, extra, side = gerar_deck_aleatorio(todas_cartas, tamanho_main=40, tamanho_extra=15, tamanho_side=15)

    if main and extra and side:
        # Salvar o deck em um único arquivo YDK
        def salvar_deck_em_ydk(nome_arquivo, main_deck, extra_deck, side_deck):
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write("#main\n")
                for carta in main_deck:
                    arquivo.write(f"{carta['id']}\n")

                arquivo.write("#extra\n")
                for carta in extra_deck:
                    arquivo.write(f"{carta['id']}\n")

                arquivo.write("!side\n")
                for carta in side_deck:
                    arquivo.write(f"{carta['id']}\n")

        # Salvar o deck em um único arquivo YDK
        salvar_deck_em_ydk("deck_completo.ydk", main, extra, side)
        print("Deck completo salvo com sucesso.")
else:
    print("Não foi possível obter as cartas.")
