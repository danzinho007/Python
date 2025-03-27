import random

# Função para gerar inimigo aleatório
def gerar_inimigo():
    return {
        "nome": "Inimigo Teste",
        "vida": 1000,
        "ataque": random.randint(50, 100),  # Ataque aleatório entre 50 e 100
        "defesa": random.randint(1, 50)     # Defesa aleatória entre 1 e 50
    }

# Definir o baralho inicial
baralho = [
    {"tipo": "ataque", "valor": 100} for _ in range(6)
] + [
    {"tipo": "defesa", "valor": 8} for _ in range(4)
] + [
    {"tipo": "buff", "efeito": "vida", "valor": 10},
    {"tipo": "buff", "efeito": "ataque", "valor": 100},
]
random.shuffle(baralho)

# Atributos do jogador
jogador = {"vida": 1000, "ataque_basico": 0, "defesa": 5, "mao": [], "descarte": []}

# Função para puxar uma carta
def puxar_carta():
    global baralho
    if not baralho:  # Se o baralho estiver vazio
        if jogador["descarte"]:
            print("\nBaralho vazio. Embaralhando cartas descartadas...")
            baralho.extend(jogador["descarte"])
            jogador["descarte"].clear()
            random.shuffle(baralho)
        else:
            return None  # Retorna None se não houver mais cartas disponíveis
    return baralho.pop()

# Função para exibir a mão
def exibir_mao():
    print("\nSua mão:")
    for i, carta in enumerate(jogador["mao"]):
        descricao = (
            f"Tipo: {carta['tipo'].capitalize()} | Valor: {carta['valor']}"
            if carta["tipo"] != "buff"
            else f"Tipo: {carta['tipo'].capitalize()} | Efeito: {carta['efeito']} | Valor: {carta['valor']}"
        )
        print(f"{i + 1}. {descricao}")

# Função para usar uma carta
def usar_carta(indice):
    if 0 <= indice < len(jogador["mao"]):
        carta = jogador["mao"].pop(indice)  # Remove a carta da mão
        jogador["descarte"].append(carta)  # Adiciona a carta ao descarte

        if carta["tipo"] == "ataque":
            dano = carta["valor"] + jogador["ataque_basico"]
            dano_real = max(0, dano - inimigo["defesa"])  # Subtrai defesa do inimigo
            inimigo["vida"] -= dano_real
            print(f"\nVocê atacou o inimigo causando {dano_real} de dano!")
        elif carta["tipo"] == "defesa":
            jogador["defesa"] += carta["valor"]
            print(f"\nVocê aumentou sua defesa em {carta['valor']}!")
        elif carta["tipo"] == "buff":
            if carta["efeito"] == "vida":
                jogador["vida"] += carta["valor"]
                print(f"\nVocê recuperou {carta['valor']} de vida!")
            elif carta["efeito"] == "ataque":
                jogador["ataque_basico"] += carta["valor"]
                print(f"\nVocê aumentou seu ataque básico em {carta['valor']}!")
    else:
        print("\nEscolha inválida!")

# Função para o inimigo atacar
def inimigo_atacar():
    ataque_inimigo = inimigo["ataque"]
    dano = ataque_inimigo - jogador["defesa"]
    dano_real = max(0, dano)  # Se o dano for negativo, o mínimo é 0
    jogador["vida"] -= dano_real
    print(f"O inimigo atacou! Você perdeu {dano_real} de vida!")

# Função para gerar o inimigo e definir o jogador
inimigo = gerar_inimigo()

# Loop do jogo
# Comprar 3 cartas iniciais
for _ in range(3):
    carta = puxar_carta()
    if carta:
        jogador["mao"].append(carta)

# Variável para contar os turnos
turno = 1

while True:
    print(f"\nTurno {turno}:")
    print(f"Inimigo: {inimigo['nome']} - Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']} | Defesa: {inimigo['defesa']}")
    print(f"Jogador: Vida: {jogador['vida']} | Defesa: {jogador['defesa']} | Ataque Básico: {jogador['ataque_basico']}")
    exibir_mao()

    # Verificar se o inimigo foi derrotado
    if inimigo["vida"] <= 0:
        print("\nParabéns! Você derrotou o inimigo.")
        break

    # Verificar se o jogador ainda pode puxar cartas
    if not baralho and not jogador["descarte"] and not jogador["mao"]:
        print("\nNão há mais cartas disponíveis. O jogo terminou!")
        break

    # Jogador puxa uma carta por turno
    nova_carta = puxar_carta()
    if nova_carta:
        jogador["mao"].append(nova_carta)

    # Jogador escolhe uma carta para usar
    if jogador["mao"]:
        escolha = int(input("\nEscolha uma carta para usar (1, 2, ...): ")) - 1
        usar_carta(escolha)

    # O inimigo ataca
    inimigo_atacar()

    # Verificar se o jogador perdeu
    if jogador["vida"] <= 0:
        print("\nVocê foi derrotado!")
        break

    # Incrementar o número de turnos
    turno += 1
