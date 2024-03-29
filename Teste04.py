import requests
from bs4 import BeautifulSoup

def get_level_info(level_url):
    # Faz uma requisição para a página da fase
    page = requests.get(level_url)

    # Analisa o HTML da página
    soup = BeautifulSoup(page.content, "html.parser")

    # Encontra o link para a página de ranking da fase
    charts_link = soup.select_one("a[href*='mode=charts']")
    
    if charts_link:
        charts_url = charts_link["href"]

        # Faz uma requisição para a página de ranking da fase
        charts_page = requests.get(charts_url)

        # Analisa o HTML da página
        charts_soup = BeautifulSoup(charts_page.content, "html.parser")

        # Encontra a tabela com os dados do ranking
        table = charts_soup.select_one("table.b")

        # Verifica se a tabela foi encontrada
        if table:
            # Encontra todas as linhas da tabela
            rows = table.select("tr")

            # Inicializa uma variável para armazenar o número de jogadores
            players_completed = 0

            # Loop através de cada linha da tabela
            for row in rows:
                # Encontra a coluna com o número de jogadores
                col = row.select_one("td:nth-of-type(5)")

                # Verifica se a coluna foi encontrada
                if col:
                    # Adiciona o número de jogadores para a variável
                    players_completed += int(col.text)

            return players_completed
    else:
        return 0
