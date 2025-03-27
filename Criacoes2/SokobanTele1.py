import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações do jogo
LARGURA_CELULA = 100  # Tamanho de cada célula
ALTURA_CELULA = 100
FPS = 30

# Mapa inicial
mapa = [
    "########",
    "T $.#  T",
    "T $.#@ T",
    "T $.#  T",
    "########"
]

# Cores (caso precise usar ao invés de imagens)
CORES = {
    "#": (0, 0, 0),        # Parede (preto)
    " ": (200, 200, 200),  # Espaço vazio (cinza claro)
    "@": (255, 255, 255),  # Jogador (branco)
    "$": (0, 0, 255),      # Caixa (azul)
    ".": (255, 255, 0),    # Objetivo (amarelo)
    "+": (200, 200, 200),  # Jogador sobre o objetivo (não usado diretamente aqui)
    "*": (0, 0, 255),      # Caixa sobre o objetivo (azul com centro amarelo)
    "T": (255, 255, 255)   # Teletransporte (branco)
}

# Carregar as imagens de emoji (substituindo os emojis com imagens PNG)
emoji_imagens = {
    "@": pygame.image.load("jogador.png"),   # Imagem do jogador
    "$": pygame.image.load("caixa.png"),     # Imagem da caixa
    ".": pygame.image.load("objetivo.png"),  # Imagem do objetivo
    "*": pygame.image.load("caixa_objetivo.png"),  # Caixa sobre objetivo
    "T": pygame.image.load("teletransporte.png"),  # Imagem do teletransporte
    "#": pygame.image.load("parede.png"),    # Imagem da parede
    " ": pygame.image.load("vazio.png"),      # Imagem de espaço vazio (corpo cinza claro ou outra imagem)
    "+": pygame.image.load("jogador_objetivo.png")  # Imagem do jogador sobre o objetivo
}

# Ajustar o tamanho das imagens para o tamanho da célula
for chave, imagem in emoji_imagens.items():
    emoji_imagens[chave] = pygame.transform.scale(imagem, (LARGURA_CELULA, ALTURA_CELULA))

# Inicialização da janela
altura = len(mapa) * ALTURA_CELULA
largura = len(mapa[0]) * LARGURA_CELULA
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sokoban com Teletransporte")

# Função para desenhar o mapa
def desenhar_mapa(tela, mapa):
    for i, linha in enumerate(mapa):
        for j, celula in enumerate(linha):
            x = j * LARGURA_CELULA
            y = i * ALTURA_CELULA
            tela.blit(emoji_imagens[celula], (x, y))

# Função para encontrar o jogador
def encontrar_jogador(mapa):
    for i, linha in enumerate(mapa):
        if "@" in linha or "+" in linha:
            return i, linha.index("@") if "@" in linha else linha.index("+")
    return None

# Função para mover o jogador
def mover_jogador(mapa, direcao, empurros):
    jogador_pos = encontrar_jogador(mapa)
    if not jogador_pos:
        return mapa, empurros

    x, y = jogador_pos
    dx, dy = 0, 0

    if direcao == "esquerda":
        dx, dy = 0, -1
    elif direcao == "direita":
        dx, dy = 0, 1
    elif direcao == "cima":
        dx, dy = -1, 0
    elif direcao == "baixo":
        dx, dy = 1, 0

    novo_x, novo_y = x + dx, y + dy

    if mapa[novo_x][novo_y] in " .T":  # Movimento para espaço válido
        if mapa[novo_x][novo_y] == "T":  # Teletransporte
            novo_y = 0 if direcao == "direita" else len(mapa[0]) - 1

        mapa[x] = mapa[x][:y] + (" " if mapa[x][y] == "@" else ".") + mapa[x][y+1:]
        mapa[novo_x] = mapa[novo_x][:novo_y] + ("@" if mapa[novo_x][novo_y] in " T" else "+") + mapa[novo_x][novo_y+1:]

    elif mapa[novo_x][novo_y] == "$":  # Empurrar caixa
        caixa_x, caixa_y = novo_x + dx, novo_y + dy
        if mapa[caixa_x][caixa_y] in " .":  # Posição atrás da caixa é válida
            mapa[novo_x] = mapa[novo_x][:novo_y] + ("@" if mapa[novo_x][novo_y] == "$" else "+") + mapa[novo_x][novo_y+1:]
            mapa[x] = mapa[x][:y] + (" " if mapa[x][y] == "@" else ".") + mapa[x][y+1:]
            mapa[caixa_x] = mapa[caixa_x][:caixa_y] + ("*" if mapa[caixa_x][caixa_y] == "." else "$") + mapa[caixa_x][caixa_y+1:]
            empurros += 1  # Incrementa o contador de empurrões

    return mapa, empurros

# Função para verificar vitória
def verificar_vitoria(mapa):
    for linha in mapa:
        if "$" in linha:  # Ainda há caixas fora dos objetivos
            return False
    return True

# Função para desenhar a contagem de objetivos, movimentos e empurrões
def desenhar_status(tela, objetivos_completos, objetivos_totais, movimentos, empurros):
    fonte = pygame.font.Font(None, 30)
    status_texto = f"Objetivos {objetivos_completos}/{objetivos_totais} Movimentos {movimentos} Empurrões {empurros}"
    texto = fonte.render(status_texto, True, (255, 255, 255))
    tela.blit(texto, (10, 10))

# Função para mostrar recordes
def desenhar_recordes(tela, recordes):
    fonte = pygame.font.Font(None, 30)
    texto_titulo = fonte.render("Recordes:", True, (255, 255, 255))
    tela.blit(texto_titulo, (10, 50))
    
    for i, (movimentos, empurros) in enumerate(recordes):
        texto_recorde = fonte.render(f"Recorde {i+1}: Movimentos: {movimentos} Empurrões: {empurros}", True, (255, 255, 255))
        tela.blit(texto_recorde, (10, 80 + i * 30))

# Lista para armazenar os recordes (movimentos, empurros)
recordes = []

# Loop principal
clock = pygame.time.Clock()
rodando = True
objetivos_completos = 0
objetivos_totais = sum(linha.count(".") for linha in mapa)
movimentos = 0
empurros = 0
esc_press = 0  # Variável para contar os pressionamentos de ESC

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Movimentos do jogador
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                mapa, empurros = mover_jogador(mapa, "esquerda",  empurros)
                movimentos += 1
            elif evento.key == pygame.K_RIGHT:
                mapa, empurros = mover_jogador(mapa, "direita", empurros)
                movimentos += 1
            elif evento.key == pygame.K_UP:
                mapa, empurros = mover_jogador(mapa, "cima", empurros)
                movimentos += 1
            elif evento.key == pygame.K_DOWN:
                mapa, empurros = mover_jogador(mapa, "baixo", empurros)
                movimentos += 1
            # Pressionamento de ESC para sair
            if evento.key == pygame.K_ESCAPE:
                esc_press += 1
                if esc_press == 2:
                    rodando = False  # Sair do jogo

    # Contagem de objetivos completados
    objetivos_completos = sum(linha.count("*") for linha in mapa)

    # Verificar vitória
    if verificar_vitoria(mapa):
        # Adicionar o recorde ao final da lista
        recordes.append((movimentos, empurros))
        recordes = sorted(recordes, key=lambda x: x[0])  # Ordena pelos movimentos
        if len(recordes) > 5:  # Limita a lista de recordes a 5
            recordes.pop()

        # Resetar o mapa para a próxima rodada
        # (aqui você pode reiniciar o mapa ou carregar um novo)
        mapa = [
            "########",
            "T $.#  T",
            "T $.#@ T",
            "T $.#  T",
            "########"
        ]
        movimentos = 0
        empurros = 0

    # Desenhar o mapa e o status
    tela.fill((0, 0, 0))  # Fundo preto
    desenhar_mapa(tela, mapa)
    desenhar_status(tela, objetivos_completos, objetivos_totais, movimentos, empurros)
    desenhar_recordes(tela, recordes)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
