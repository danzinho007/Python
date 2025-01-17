import requests

def obter_cartas_por_conjunto(conjunto_nome):
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?set={conjunto_nome}"
    response = requests.get(url)

    if response.status_code == 200:
        cartas_do_conjunto = response.json()['data']
        return [carta['id'] for carta in cartas_do_conjunto]
    else:
        print(f"Erro na solicitação: {response.status_code}")
        return None

conjunto_nome = "Legend of Blue Eyes White Dragon"

# Obtém os IDs das cartas do conjunto especificado
ids_cartas = obter_cartas_por_conjunto(conjunto_nome)

if ids_cartas:
    # Converte os IDs para strings e salva em um arquivo, 1 em cada linha
    with open(f"{conjunto_nome}_ids.txt", "w") as file:
        file.write("\n".join(map(str, ids_cartas)))
    print(f"IDs das cartas do conjunto '{conjunto_nome}' salvos com sucesso.")
else:
    print(f"Não foi possível obter as cartas do conjunto '{conjunto_nome}'.")
