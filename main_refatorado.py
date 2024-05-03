import requests
from bs4 import BeautifulSoup


# h2_elements = soup.find_all('h2')

# for h2 in h2_elements:
#     link = h2.find('a')
#     href =  link.get('href').replace('\\', '').replace('\"', '')
#     url = f"https://www.defesacivil.rs.gov.br{href}"

#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     h1_elements = soup.find('h1', class_='artigo__titulo')
#     div_elements = soup.find('div', class_='artigo__texto')
    
#     print(f'Url: {url}\n')
#     print(f'Titulo: {h1_elements.text}\n')
#     print(f'Artigo: {div_elements.text}\n')
#     print('----------------------------------------------\n')

def scrape_urls(url):
    articles_url = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for h2 in soup.find_all('h2'):
            link = h2.find('a')
            href =  link.get('href').replace('\\', '').replace('\"', '')

            articles_url.append(f"https://www.defesacivil.rs.gov.br{href}")
    return articles_url

def fetch_article_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_element = soup.find('h1', class_='artigo__titulo')
        content_element = soup.find('div', class_='artigo__texto')

        if title_element and content_element:
            title = title_element.text.strip()
            content = content_element.text.strip()
            return title, content
        
    return None, None

def main():
    url = "https://www.defesacivil.rs.gov.br/_service/conteudo/pagedlistfilho?id=107&templatename=pagina.listanoticia.padrao&currentPage=2&pageSize=10&fields%5B%5D=Titulo&fields%5B%5D=TituloCurto&fields%5B%5D=Texto&form%5Bpagina%5D=2&form%5Bordem%5D=RECENTES"
    articles_url = scrape_urls(url)
    for article_url in articles_url:
        title, content = fetch_article_content(article_url)
        if title and content:
            print(f'Url: {article_url}\n')
            print(f'Titulo: {title}\n')
            print(f'Artigo: {content}\n')
            print('----------------------------------------------\n')


if __name__ == '__main__':
    main()