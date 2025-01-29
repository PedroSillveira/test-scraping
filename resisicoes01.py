import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

# REQUISIÇÃO
response = requests.get('https://g1.globo.com/')
# CONVERSÃO DE CONTEÚDO PARA OBJETO DO BEATIFULSOUP
content = response.content
# OBJETO
site = BeautifulSoup(content, 'html.parser')
# RESPOSTA DA BUSCA ATRAVES DA CLASS
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

  
    # TITULO RESPOSTA ESPECIFICA ATRAVES DA VARIAVEL JA CRIADA COM BUSCA ESPECIFICA
    titulo = noticia.find('a', attrs={'class', 'feed-post-link'}) 
    print(titulo.text)
    print(titulo['href']) #ACESSO AO LINK DA NOTICIA

    # SUBTITULO
    subtitulo = noticia.find('a', attrs={'class', 'feed-post-body-title'}) 
    
    if(subtitulo):
        print(subtitulo.text)

