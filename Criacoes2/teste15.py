import statistics

# -----------------------------------------
# Leitor de arquivos .ydk
# -----------------------------------------
def carregar_deck(caminho):
    main = []
    extra = []
    side = []
    modo = "main"

    with open(caminho, "r", encoding="utf8") as f:
        for linha in f:
            linha = linha.strip()

            if linha == "#main":
                modo = "main"
                continue
            elif linha == "#extra":
                modo = "extra"
                continue
            elif linha == "!side":
                modo = "side"
                continue
            elif linha.startswith("#") or linha == "":
                continue

            if modo == "main":
                main.append(linha)
            elif modo == "extra":
                extra.append(linha)
            else:
                side.append(linha)

    return main, extra, side


# -----------------------------------------
# Banco simples de ATK/DEF (exemplo)
# Você pode expandir depois
# -----------------------------------------
import requests

def obter_status_carta(card_id):
    """Retorna ATK/DEF consultando a API pública do YGOPRODeck."""
    try:
        r = requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?id={card_id}", timeout=5)
        dados = r.json()

        carta = dados['data'][0]
        atk = carta.get('atk', 0)
        dfn = carta.get('def', 0)

        return atk if atk != None else 0, dfn if dfn != None else 0
    except:
        return 0, 0


# -----------------------------------------
# Cálculo das métricas
# -----------------------------------------
def analisar_deck(main):
    atks = []
    dfs  = []

    for cid in main:
        atk, dfn = obter_status_carta(cid)
        atks.append(atk)
        dfs.append(dfn)

    media_atk = statistics.mean(atks) if atks else 0
    media_def = statistics.mean(dfs) if dfs else 0

    monstros = len([x for x in atks if x > 0])
    magias_armadilhas = len(main) - monstros

    proporcao = monstros / len(main) if main else 0

    return {
        "media_atk": media_atk,
        "media_def": media_def,
        "monstros": monstros,
        "spells_traps": magias_armadilhas,
        "proporcao_monstros": proporcao
    }


# -----------------------------------------
# Fórmula estilo WC2008 (minha simulação)
# -----------------------------------------
def calcular_rating(info):
    """
    Rating aproximado estilo WC2008:
    500 = fraco
    600 = abaixo da média
    750 = médio
    900 = forte
    1000 = muito forte
    """

    score = 0

    # ATK médio pesa bastante
    if info["media_atk"] < 1000:
        score += 100
    elif info["media_atk"] < 1500:
        score += 200
    elif info["media_atk"] < 2000:
        score += 300
    else:
        score += 400

    # Proporção de monstros
    if info["proporcao_monstros"] < 0.3:
        score += 50
    elif info["proporcao_monstros"] < 0.5:
        score += 100
    else:
        score += 150

    # Número total de cartas — decks inconsistentes são penalizados
    score += min(200, info["monstros"] * 5)

    # Conversão para escala tipo WC2008
    if score < 300:
        return 500
    elif score < 450:
        return 600
    elif score < 600:
        return 750
    elif score < 800:
        return 900
    else:
        return 1000


# -----------------------------------------
# Execução
# -----------------------------------------
if __name__ == "__main__":
    caminho = input("Digite o caminho do seu deck .ydk: ")

    main, extra, side = carregar_deck(caminho)
    info = analisar_deck(main)
    rating = calcular_rating(info)

    print("\n===== RESULTADO =====")
    print("Cartas no Main:", len(main))
    print("Média ATK:", round(info["media_atk"], 2))
    print("Média DEF:", round(info["media_def"], 2))
    print("Proporção de monstros:", round(info["proporcao_monstros"] * 100, 1), "%")
    print("Rating estilo WC2008:", rating)
