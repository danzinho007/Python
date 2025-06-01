print("Copa do Mundo - Simulação de Confrontos")
def escolher_classificados(grupos):
    classificados = {}
    print("\nEscolha 2 classificados para cada grupo:")
    for grupo, times in grupos.items():
        print(f"\n{grupo}: {', '.join(times)}")
        selecao = []
        while len(selecao) < 2:
            escolha = input(f"Escolha o {len(selecao)+1}º classificado do grupo {grupo}: ").strip()
            if escolha in times and escolha not in selecao:
                selecao.append(escolha)
            else:
                print("Escolha inválida ou já selecionada. Tente novamente.")
        classificados[grupo] = selecao
    return classificados

def decidir_confrontos(confrontos, classificados, fase_nome):
    vencedores = {}
    print(f"\n=== {fase_nome.upper()} ===")
    for chave, (grupo1, pos1, grupo2, pos2) in confrontos.items():
        time1 = classificados[grupo1][pos1]
        time2 = classificados[grupo2][pos2]
        print(f"\nConfronto {chave}: {time1} vs {time2}")
        while True:
            vencedor = input("Quem vence? ").strip()
            if vencedor == time1 or vencedor == time2:
                vencedores[chave] = vencedor
                break
            else:
                print("Escolha inválida. Tente novamente.")
    return vencedores

# Definir grupos
grupos = {
    "Grupo_A": ["Al Ahlhly", "Inter Miami", "Palmeiras", "Porto"],
    "Grupo_B": ["Altético de Madrid", "Botafogo", "PSG", "Seatle Sounders"],
    "Grupo_C": ["Auckland City", "Bayern de Munique", "Benfica", "Boca Juniors"],
    "Grupo_D": ["Chelsea", "Esperance", "Flamengo", "Los Angeles"],
    "Grupo_E": ["Internazionale", "Monterrey", "River Plate", "Urawa Reds"],
    "Grupo_F": ["Borussia Dortmund", "Fluminense", "Mamelodi Sundowns", "UlsanHD"],
    "Grupo_G": ["AlAin", "Juventus", "Manchester City", "Wydad Casablanca"],
    "Grupo_H": ["AlHilal", "Pachuca", "RB Salzbur", "RealMadrid"]
}

# Escolher classificados
classificados = escolher_classificados(grupos)

# Definir confrontos das OITAVAS (chave: (grupo, posição[0=1°,1=2°]))
oitavas = {
    "O1": ("GrupoA", 0, "GrupoB", 1),
    "O2": ("GrupoC", 0, "GrupoD", 1),
    "O3": ("GrupoE", 0, "GrupoF", 1),
    "O4": ("GrupoG", 0, "GrupoH", 1),
    "O5": ("GrupoB", 0, "GrupoA", 1),
    "O6": ("GrupoD", 0, "GrupoC", 1),
    "O7": ("GrupoF", 0, "GrupoE", 1),
    "O8": ("GrupoH", 0, "GrupoG", 1),
}

vencedores_oitavas = decidir_confrontos(oitavas, classificados, "Oitavas de Final")

# Definir QUARTAS com base nos vencedores das oitavas
quartas = {
    "Q1": ("O1", "O2"),
    "Q2": ("O3", "O4"),
    "Q3": ("O5", "O6"),
    "Q4": ("O7", "O8"),
}

vencedores_quartas = {}
print("\n=== QUARTAS DE FINAL ===")
for chave, (jogo1, jogo2) in quartas.items():
    time1 = vencedores_oitavas[jogo1]
    time2 = vencedores_oitavas[jogo2]
    print(f"\nConfronto {chave}: {time1} vs {time2}")
    while True:
        vencedor = input("Quem vence? ").strip()
        if vencedor == time1 or vencedor == time2:
            vencedores_quartas[chave] = vencedor
            break
        else:
            print("Escolha inválida. Tente novamente.")

# Semifinais
semis = {
    "S1": ("Q1", "Q2"),
    "S2": ("Q3", "Q4")
}

vencedores_semis = {}
perdedores_semis = {}
print("\n=== SEMIFINAIS ===")
for chave, (jogo1, jogo2) in semis.items():
    time1 = vencedores_quartas[jogo1]
    time2 = vencedores_quartas[jogo2]
    print(f"\nConfronto {chave}: {time1} vs {time2}")
    while True:
        vencedor = input("Quem vence? ").strip()
        if vencedor == time1 or vencedor == time2:
            vencedores_semis[chave] = vencedor
            perdedores_semis[chave] = time1 if vencedor == time2 else time2
            break
        else:
            print("Escolha inválida. Tente novamente.")

# Final
print("\n=== FINAL ===")
finalista1 = vencedores_semis["S1"]
finalista2 = vencedores_semis["S2"]
print(f"\n{finalista1} vs {finalista2}")
while True:
    campeao = input("Quem vence a FINAL? ").strip()
    if campeao == finalista1 or campeao == finalista2:
        vice = finalista1 if campeao == finalista2 else finalista2
        break
    else:
        print("Escolha inválida. Tente novamente.")

# Terceiro lugar
print("\n=== DISPUTA DE 3º LUGAR ===")
terceiro1 = perdedores_semis["S1"]
terceiro2 = perdedores_semis["S2"]
print(f"\n{terceiro1} vs {terceiro2}")
while True:
    terceiro = input("Quem vence o 3º lugar? ").strip()
    if terceiro == terceiro1 or terceiro == terceiro2:
        break
    else:
        print("Escolha inválida. Tente novamente.")

# Resultado final
print("\n=== RESULTADO FINAL ===")
print(f"🥇 Campeão: {campeao}")
print(f"🥈 Vice-campeão: {vice}")
print(f"🥉 Terceiro lugar: {terceiro}")
