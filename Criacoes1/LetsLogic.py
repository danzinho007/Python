import requests
import pandas as pd
import time

# Sua chave de API
API_KEY = ""

# URLs da API
BASE_URL = "https://letslogic.com/api/v1"
COLLECTIONS_URL = f"{BASE_URL}/collections"
LEVELS_URL = f"{BASE_URL}/collection"

# Lista para armazenar dados de níveis
all_levels = []

# Obter lista de coleções
print("Obtendo coleções...")
collections_response = requests.post(f"{COLLECTIONS_URL}?key={API_KEY}")  # Passando a chave na URL

if collections_response.status_code == 200:
    try:
        collections = collections_response.json()
        print(f"Número de coleções obtidas: {len(collections)}")
        print(f"Primeira coleção (raw): {collections[0]}")  # Exibe a primeira coleção para inspeção
    except requests.exceptions.JSONDecodeError:
        print("Erro ao decodificar a resposta como JSON.")
        print("Resposta bruta:", collections_response.text)
        collections = []  # Define uma lista vazia
else:
    print(f"Erro ao obter coleções. Código HTTP: {collections_response.status_code}")
    print("Resposta bruta:", collections_response.text)
    collections = []  # Define uma lista vazia

if not collections:
    print("Nenhuma coleção foi encontrada ou ocorreu um erro. Encerrando.")
else:
    for collection in collections:
        # Usando 'title' para obter o nome da coleção
        collection_id = collection.get("id")
        collection_name = collection.get("title", "Nome não disponível")  # Usando 'title' para o nome

        print(f"Processando coleção: {collection_name} (ID: {collection_id})")

        # Obter níveis na coleção
        levels_response = requests.post(f"{LEVELS_URL}/{collection_id}?key={API_KEY}")  # Passando a chave na URL
        if levels_response.status_code == 200:
            try:
                levels = levels_response.json()
                for level in levels:
                    level_id = level.get("id")
                    title = level.get("title")
                    
                    # Tentando acessar 'completed' de forma segura
                    completions = level.get("completed", 0)  # Ajuste se necessário
                    if isinstance(completions, dict):
                        completions = completions.get("completed_count", 0)  # Caso 'completed' seja um dicionário
                    likes = level.get("likes", 0)
                    total_points = level.get("total_points", 0)

                    all_levels.append({
                        "Coleção": collection_name,
                        "ID do Mapa": level_id,
                        "Título": title,
                        "Completados": completions,
                        "Curtidas": likes,
                        "Pontos Totais": total_points
                    })
            except requests.exceptions.JSONDecodeError:
                print(f"Erro ao decodificar níveis para a coleção {collection_name}.")
                print("Resposta bruta:", levels_response.text)
        else:
            print(f"Erro ao obter níveis da coleção {collection_name}. Código HTTP: {levels_response.status_code}")
            print("Resposta bruta:", levels_response.text)

        # Evitar sobrecarregar a API
        time.sleep(1)

# Salvar os dados coletados, se houver
if all_levels:
    df = pd.DataFrame(all_levels)
    df = df.sort_values(by="Completados", ascending=False)
    df.to_csv("mapas_classificados.csv", index=False)
    print("Dados coletados e salvos no arquivo 'mapas_classificados.csv'.")
else:
    print("Nenhum dado foi coletado.")
