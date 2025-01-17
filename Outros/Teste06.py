import requests
from bs4 import BeautifulSoup

def get_level_info(level_url):
    # Faz uma requisição para a página da fase
    page = requests.get(level_url)
    
    # Cria um objeto BeautifulSoup a partir do conteúdo da página
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Encontra o link para a página de rankings da fase
    more_link = soup.find("a", string="more")
    if more_link:
        more_url = more_link["href"]
    else:
        print("Link 'more' não encontrado na página.")
    return None

    # Faz uma requisição para a página de rankings da fase
    more_page = requests.get(more_url)

    # Cria um objeto BeautifulSoup a partir do conteúdo da página de rankings
    more_soup = BeautifulSoup(more_page.content, "html.parser")
   
    # Encontra todas as linhas da tabela na página "more"
    rows = more_soup.find("table").find_all("tr")
    
    # Percorre cada linha da tabela e extrai as informações
    players_completed = []
    for row in rows[1:]:
        cells = row.find_all("td")
        player = cells[0].text
        completed = cells[1].text
        players_completed.append((player, completed))
    
    return players_completed
    
level_url = "http://example.com/level/1"
players_completed = get_level_info(level_url)
print(players_completed)
