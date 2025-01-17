import requests
from bs4 import BeautifulSoup

def get_level_info(level_url):
    # Faz uma requisição para a página da fase
    page = requests.get(level_url)
    
    # Cria um objeto BeautifulSoup a partir do conteúdo da página
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Encontra o link para a página de rankings da fase
    more_link = soup.find("a", text="more")

    # Pega o valor do atributo "href" do link
    more_url = more_link["href"]
    
    # Faz uma requisição para a página de rankings da fase
    more_page = requests.get(more_url)

    # Cria um objeto BeautifulSoup a partir do conteúdo da página de rankings
    more_soup = BeautifulSoup(more_page.content, "html.parser")
   
    # Encontra o número de jogadores que completaram a fase
    more_table = more_soup.find("table", class_="sok-table")
    more_rows = more_table.find_all("tr")
    players_completed = len(more_rows) - 1
    
    return players_completed

level_urls = [f"http://www.game-sokoban.com/index.php?mode=level&lid={i}" for i in range(1, 100000)]

for level_url in level_urls:
    players_completed = get_level_info(level_url)
    print(f"{level_url}: {players_completed}")
