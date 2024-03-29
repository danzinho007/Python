import requests
from bs4 import BeautifulSoup


def get_level_rankings(level_url):
    # Faz uma requisição para a página da fase
    page = requests.get(level_url)

    # Verifica se a requisição foi bem-sucedida
    if page.status_code == 200:
        # Analisa o conteúdo da página usando BeautifulSoup
        soup = BeautifulSoup(page.content, "html.parser")

        # Obtém o link para a página de ranking da fase
        link = soup.find("a", text="charts").get("href")
        url = "http://www.game-sokoban.com" + link

        # Faz uma requisição para a página de ranking da fase
        page = requests.get(url)

        # Busca o link para a página "charts"
        link = soup.find("a", string="charts").get("href")

        # Verifica se a requisição foi bem-sucedida
        if page.status_code == 200:
            # Analisa o conteúdo da página usando BeautifulSoup
            soup = BeautifulSoup(page.content, "html.parser")

            # Obtém o ranking de conclusões da fase
            ranking = soup.find("table", class_="ranking").find_all("tr")[1:]

            # Armazena o número de jogadores para cada posição no ranking
            players = [int(rank.find_all("td")[2].text) for rank in ranking]

            return players

# Faz uma requisição para obter o conteúdo da página inicial
url = "http://www.game-sokoban.com/index.php?mode=phome"
page = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if page.status_code == 200:
    # Analisa o conteúdo da página usando BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtém o link para a página de catálogo de coleções
    link = soup.find("a", string="catalog")
    if link:
        link = link.get("href")
    else:
        link = None

    # Faz uma requisição para obter o conteúdo da página de catálogo de coleções
    page = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if page.status_code == 200:
        # Analisa o conteúdo da página usando BeautifulSoup
            soup = BeautifulSoup(page.content, "html.parser")
