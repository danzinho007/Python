import requests
from bs4 import BeautifulSoup

# URL do catálogo
catalog_url = "http://www.game-sokoban.com/?mode=catalog&cid=346"

# Faz uma requisição para a página do catálogo
page = requests.get(catalog_url)

# Verifica se a requisição foi bem-sucedida
if page.status_code == 200:
    # Analisa o conteúdo da página usando BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")

    # Encontra todos os links para as fases
    level_links = soup.find_all("a", class_="level_link")
    
    # Loop através de cada link de fase
    for level_link in level_links:
        # URL da fase
        level_url = level_link["href"]
        
        # Faz uma requisição para a página da fase
        page = requests.get(level_url)
        
        # Verifica se a requisição foi bem-sucedida
        if page.status_code == 200:
            # Analisa o conteúdo da página usando BeautifulSoup
            soup = BeautifulSoup(page.content, "html.parser")
            
            # Encontra o link para o ranking da fase
            charts_link = soup.find("a", string="charts")
            
            # Verifica se o link foi encontrado
            if charts_link:
                # URL do ranking da fase
                charts_url = charts_link["href"]
                
                # Faz uma requisição para a página de ranking da fase
                page = requests.get(charts_url)
                
                # Verifica se a requisição foi bem-sucedida
                if page.status_code == 200:
                    # Analisa o conteúdo da página usando BeautifulSoup
                    soup = BeautifulSoup(page.content, "html.parser")
                    
                    # Aqui você pode acessar as informações do ranking e classificá-las como desejado.
                    # ...
                else:
                    print("Erro ao acessar a página de ranking da fase")
            else:
                print("Link para o ranking da fase não encontrado")
        else:
            print("Erro ao acessar a página da fase")
else:
    print("Erro ao acessar a página do catálogo")

