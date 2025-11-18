import statistics
import requests

# -----------------------------------------
# Função para ler deck .ydk
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
# Função para obter ATK/DEF de uma carta usando YGOPRODeck API
# -----------------------------------------
def obter_status_carta(card_id):
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
# Função para analisar deck
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
# Função de cálculo de rating ajustável
# -----------------------------------------
def calcular_rating(info, pesos):
    score = 0
    score += pesos['atk'] * info['media_atk']
    score += pesos['monstro'] * info['proporcao_monstros'] * 1000
    score += pesos['quantidade'] * info['monstros']
    score += pesos['spelltrap'] * info['spells_traps']

    # Nova escala simulando WC2008 real
    if score < 500:
        return 500
    elif score < 700:
        return 600
    elif score < 900:
        return 750
    elif score < 1100:
        return 900
    elif score < 1300:
        return 1000
    elif score < 1500:
        return 1200
    elif score < 1650:
        return 1500
    elif score < 1750:
        return 1600
    elif score < 1800:
        return 1700
    else:
        return 1800

# -----------------------------------------
# Função interativa para ajustar pesos
# -----------------------------------------
def ajustar_pesos(pesos):
    print("\n===== Ajuste os pesos das métricas (0 a 1) =====")
    for chave in pesos:
        try:
            valor = float(input(f"{chave} (atual {pesos[chave]}): "))
            if 0 <= valor <= 1:
                pesos[chave] = valor
        except:
            print("Valor inválido. Mantendo o peso atual.")
    return pesos

# -----------------------------------------
# Execução principal
# -----------------------------------------
if __name__ == "__main__":
    caminho = input("Digite o caminho do seu deck .ydk: ")
    main, extra, side = carregar_deck(caminho)
    info = analisar_deck(main)

    pesos = {
    'atk': 729.284,
    'monstro': 1507.369,
    'quantidade': 61.802,
    'spelltrap': 1.545
    }  

    while True:
        rating = calcular_rating(info, pesos)
        print("\n===== RESULTADO =====")
        print("Cartas no Main:", len(main))
        print("Média ATK:", round(info["media_atk"], 2))
        print("Média DEF:", round(info["media_def"], 2))
        print("Proporção de monstros:", round(info["proporcao_monstros"] * 100, 1), "%")
        print("Rating estilo WC2008:", rating)

        opcao = input("\nQuer ajustar os pesos para recalcular? (s/n): ").lower()
        if opcao == 's':
            pesos = ajustar_pesos(pesos)
        else:
            break
