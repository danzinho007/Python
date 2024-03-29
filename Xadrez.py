tabuleiro = [
  ["T", "C", "B", "Q", "K", "B", "C", "T"],
  ["P", "P", "P", "P", "P", "P", "P", "P"],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  ["P", "P", "P", "P", "P", "P", "P", "P"],
  ["T", "C", "B", "Q", "K", "B", "C", "T"]
]

def posicao_valida(tabuleiro, posicao, jogador_atual):
  # Verifique se a posição está no tabuleiro
  if posicao[0] < 0 or posicao[0] > 7 or posicao[1] < 0 or posicao[1] > 7:
    return False

  # Verifique se existe uma peça na posição
  if tabuleiro[posicao[0]][posicao[1]] == " ":
    return False

  # Verifique se a peça é do jogador atual
  if jogador_atual == "branco":
    if tabuleiro[posicao[0]][posicao[1]].isupper():
      return True
    else:
      return False
  else:
    if tabuleiro[posicao[0]][posicao[1]].islower():
      return True
    else:
      return False

def movimento_valido_peao(tabuleiro, linha_atual, coluna_atual, linha_nova, coluna_nova):
  # Verifica se o movimento é para a frente
  if linha_nova > linha_atual:
    # Verifica se o peão está se movendo para uma casa vazia
    if tabuleiro[linha_nova][coluna_nova] == " ":
      # Verifica se o peão está se movendo uma casa para frente
      if linha_nova == linha_atual + 1:
        return True
      # Se o peão está se movendo duas casas para frente, precisamos verificar se a casa de partida está vazia
      elif linha_nova == linha_atual + 2 and tabuleiro[linha_atual + 1][coluna_atual] == " ":
        return True
  return False

# O bispo só pode se mover em diagonal
  if abs(posicao_final[0] - posicao_inicial[0]) !=0:
    if abs(posicao_final[1] - posicao_inicial[1]) !=0:
      print("Movimento inválido para o bispo.")
      return
  elif peca == "N":
    # O cavalo se move em "L"
    if (abs(posicao_final[0] - posicao_inicial[0]) == 2 and abs(posicao_final[1] - posicao_inicial[1]) == 1) or (abs(posicao_final[0] - posicao_inicial[0]) == 1 and abs(posicao_final[1] - posicao_inicial[1]) == 2):
      pass
    else:
      print("Movimento inválido para o cavalo.")
      return
  elif peca == "Q":
    # A rainha pode se mover em qualquer direção em linha reta ou diagonal
    if posicao_final[0] != posicao_inicial[0] and posicao_final[1] != posicao_inicial[1] and abs(posicao_final[0] - posicao_inicial[0]) != abs(posicao_final[1] - posicao_inicial[1]):
      print("Movimento inválido para a rainha.")
      return
  elif peca == "K":
    # O rei só pode se mover para a casa adjacente
    if abs(posicao_final[0] - posicao_inicial[0]) > 1 or abs(posicao_final[1] - posicao_inicial[1]) > 1:
      print("Movimento inválido para o rei.")
      return
  else:
    print("Não há peça na posição inicial.")
    return

    'python'
    