import requests
from bs4 import BeautifulSoup


url = "https://www.defesacivil.rs.gov.br/_service/conteudo/pagedlistfilho?id=107&templatename=pagina.listanoticia.padrao&currentPage=2&pageSize=10&fields%5B%5D=Titulo&fields%5B%5D=TituloCurto&fields%5B%5D=Texto&form%5Bpagina%5D=2&form%5Bordem%5D=RECENTES"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

h2_elements = soup.find_all('h2')

for h2 in h2_elements:
    link = h2.find('a')
    href =  link.get('href').replace('\\', '').replace('\"', '')
    url = f"https://www.defesacivil.rs.gov.br{href}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    h1_elements = soup.find('h1', class_='artigo__titulo')
    div_elements = soup.find('div', class_='artigo__texto')
    
    print(f'Url: {url}\n')
    print(f'Titulo: {h1_elements.text}\n')
    print(f'Artigo: {div_elements.text}\n')
    print('----------------------------------------------\n')
