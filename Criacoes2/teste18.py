import statistics
import os

# -----------------------------------------
# Carregar deck .ydk
# -----------------------------------------
def carregar_deck(caminho):
    if not os.path.isfile(caminho):
        print(f"Arquivo não encontrado: {caminho}")
        return []
    main = []
    modo = "main"
    with open(caminho, "r", encoding="utf8") as f:
        for linha in f:
            linha = linha.strip()
            if linha == "#main":
                modo = "main"
                continue
            elif linha.startswith("#") or linha == "":
                continue
            if modo == "main":
                main.append(linha)
    return main

# -----------------------------------------
# Analisar deck (atributos principais)
# Para usar real, substitua por API YGOPRODeck
# -----------------------------------------
def analisar_deck(main):
    atks = []
    monstros = 0

    for cid in main:
        try:
            card_id = int(cid)
            # Aqui você pode colocar chamada real à API YGOPRODeck
            atk = card_id % 1000  # Simulação provisória
            atks.append(atk)
            if atk > 0:
                monstros += 1
        except:
            # Se não for número, ignora
            continue

    media_atk = sum(atks) / len(atks) if atks else 0
    proporcao_monstros = monstros / len(main) if main else 0
    spelltrap = len(main) - monstros
    return media_atk, proporcao_monstros, monstros, spelltrap

# -----------------------------------------
# Calcular pesos via sistema proporcional
# -----------------------------------------
def calibrar_pesos_multi(deck_infos, ratings):
    # deck_infos: lista de tuplas (atk, prop, qtd, st)
    # ratings: lista de ratings reais do jogo
    n = len(deck_infos)
    sum_atk = sum([atk for atk, prop, qtd, st in deck_infos])
    sum_prop = sum([prop*1000 for atk, prop, qtd, st in deck_infos])
    sum_qtd = sum([qtd for atk, prop, qtd, st in deck_infos])
    sum_st  = sum([st for atk, prop, qtd, st in deck_infos])
    sum_rating = sum(ratings)

    # Pesos proporcionais médios
    peso_atk = sum_rating * (sum_atk / (sum_atk + sum_prop + sum_qtd + sum_st))
    peso_monstro = sum_rating * (sum_prop / (sum_atk + sum_prop + sum_qtd + sum_st))
    peso_quantidade = sum_rating * (sum_qtd / (sum_atk + sum_prop + sum_qtd + sum_st))
    peso_spelltrap = sum_rating * (sum_st / (sum_atk + sum_prop + sum_qtd + sum_st))

    return peso_atk, peso_monstro, peso_quantidade, peso_spelltrap

# -----------------------------------------
# Execução principal
# -----------------------------------------
if __name__ == "__main__":
    deck_infos = []
    ratings = []

    while True:
        caminho = input("Digite o caminho do deck .ydk (ou 'fim' para encerrar): ")
        if caminho.lower() == "fim":
            break
        main = carregar_deck(caminho)
        if not main:
            continue

        atk, prop, qtd, st = analisar_deck(main)
        print(f"ATK médio: {atk:.2f}, Proporção monstros: {prop*100:.1f}%, Quantidade: {qtd}, Spell/Trap: {st}")

        rating_jogo = float(input("Digite o rating real do jogo para este deck: "))
        deck_infos.append((atk, prop, qtd, st))
        ratings.append(rating_jogo)

    if not deck_infos:
        print("Nenhum deck carregado.")
        exit()

    pesos = calibrar_pesos_multi(deck_infos, ratings)
    print("\n===== Pesos calibrados médios =====")
    print(f"ATK: {pesos[0]:.3f}")
    print(f"Monstro: {pesos[1]:.3f}")
    print(f"Quantidade: {pesos[2]:.3f}")
    print(f"Spell/Trap: {pesos[3]:.3f}")
