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

conjunto_nome_blue_eyes = "Legend of Blue Eyes White Dragon"
conjunto_nome_metal_raiders = "Metal Raiders"
conjunto_nome_spell_ruler = "Spell Ruler"
conjunto_nome_pharaohs_servant = "Pharaoh's Servant"

# Obtém os IDs das cartas dos conjuntos especificados
ids_blue_eyes = obter_cartas_por_conjunto(conjunto_nome_blue_eyes)
ids_metal_raiders = obter_cartas_por_conjunto(conjunto_nome_metal_raiders)
ids_spell_ruler = obter_cartas_por_conjunto(conjunto_nome_spell_ruler)
ids_pharaohs_servant = obter_cartas_por_conjunto(conjunto_nome_pharaohs_servant)

if ids_blue_eyes and ids_metal_raiders and ids_spell_ruler and ids_pharaohs_servant:
    # Obtém os IDs das cartas do conjunto "Pharaoh's Servant" que não estão nos conjuntos "Legend of Blue Eyes White Dragon", "Metal Raiders" e "Spell Ruler"
    ids_diferentes = set(ids_pharaohs_servant) - set(ids_blue_eyes) - set(ids_metal_raiders) - set(ids_spell_ruler)

    # Converte os IDs para strings e salva em um arquivo, 1 em cada linha
    with open(f"Pharaohs_Servant_not_in_Blue_Eyes_or_Metal_Raiders_or_Spell_Ruler_ids.txt", "w") as file:
        file.write("\n".join(map(str, ids_diferentes)))
    print(f"IDs das cartas do conjunto 'Pharaoh's Servant' que não estão nos conjuntos 'Legend of Blue Eyes White Dragon', 'Metal Raiders' e 'Spell Ruler' foram salvos com sucesso.")
else:
    print("Não foi possível obter os IDs das cartas de pelo menos um dos conjuntos.")
