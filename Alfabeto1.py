from string import ascii_uppercase

# Lista de letras do alfabeto
letras = list(ascii_uppercase)

def gerar_sequencia(letras, tamanho):
    sequencia = ['A'] * tamanho

    while True:
        # Gere a sequência atual
        combinacao = ''.join(sequencia)
        yield combinacao

        # Atualize a sequência para a próxima
        for i in range(tamanho - 1, -1, -1):
            if sequencia[i] == 'Z':
                sequencia[i] = 'A'
            else:
                sequencia[i] = letras[letras.index(sequencia[i]) + 1]
                break

# Tamanho da sequência desejada
tamanho_sequencia = 3

# Gere as sequências
gerador = gerar_sequencia(letras, tamanho_sequencia)
for _ in range(len(letras) ** tamanho_sequencia):
    print(next(gerador))

Bolsa Marsupial =
Carvão Mineral = Sul
Don Quixote = Sancho Pança
Eramos Seis = Silvio de Abreu
Michael Jackson = Jackson Five
Miopes = Lente Divergente
Petróleo = Rio de Janeiro
Pombo = arrulha
Quantidade de Chuva = Precipitação
Teórico Político XVIII = John Locke
Torre dos Muçulmanos = Minarete


Jungle Rose / Rosa da Selva = Item que pode ser colhido na Selva
Desktop Introduzido
1.0.4 Item de toucador
https://terraria.fandom.com/wiki/Jungle_Rose


967.140.655.691.703.339.764.940.800
2.000.000.000