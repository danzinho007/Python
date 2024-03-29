import requests
from bs4 import BeautifulSoup

def get_level_info(level_url):
    # Faz uma requisição para a página da fase
    page = requests.get(level_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Encontra o link para a página more (charts)
    charts_link = soup.find("a", string="more (charts)")
    charts_url = charts_link["href"]

    # Faz uma requisição para a página more (charts)
    charts_page = requests.get(charts_url)
    charts_soup = BeautifulSoup(charts_page.content, 'html.parser')

    # Encontra o número de jogadores que concluíram a fase
    players_completed = charts_soup.find("td", string="Players completed").find_next_sibling().text

    return players_completed

# Gera a URL para cada fase
level_urls = [f"http://www.game-sokoban.com/index.php?mode=level&lid={i}" for i in range(1, 100000)]

# Loop através de cada fase
for level_url in level_urls:
    players_completed = get_level_info(level_url)
    print(f"{level_url}: {players_completed} jogadores concluíram a fase")
