from datetime import datetime, timedelta

# Data inicial para começar a contagem
data_inicial = datetime(2024, 11, 13)  # 9 de dezembro de 2024
data_final = datetime(2025, 1, 6)    # 31 de janeiro de 2025

# Variáveis auxiliares
contador_dia = 1  # Número do dia
data_atual = data_inicial

# Exibindo o ano inicial
print(data_inicial.year)

# Loop para gerar as datas e dias
while data_atual <= data_final:
    # Formatando e exibindo a data e o número do dia
    print(f"{data_atual.strftime('%d/%m')} = Dia {contador_dia:02d}")
    
    # Avança para o próximo dia
    data_atual += timedelta(days=1)
    contador_dia += 1
    
    # Quando mudar o ano, exibir o novo ano
    if data_atual.day == 1 and data_atual.month == 1:
        print(data_atual.year)
