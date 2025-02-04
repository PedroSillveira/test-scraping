import requests  
# Biblioteca para fazer requisições HTTP
from bs4 import BeautifulSoup  
# Biblioteca para fazer parsing de HTML
import sys  
# Biblioteca para manipulação do sistema



# Configura a saída do terminal para suportar caracteres especiais (UTF-8)
sys.stdout.reconfigure(encoding='utf-8')

# Faz uma requisição HTTP para obter o conteúdo da página do G1
response = requests.get('https://g1.globo.com/')

# Obtém o conteúdo HTML da página
content = response.content

# Faz o parsing do HTML utilizando BeautifulSoup
site = BeautifulSoup(content, 'html.parser')

# Encontra a primeira notícia na página, baseada na estrutura do site
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# Extrai o título da notícia
titulo = noticia.find('a', attrs={'class', 'feed-post-link'})

# Exibe o título no console
print(titulo.text)

# Extrai o subtítulo da notícia
subtitulo = noticia.find('a', attrs={'class', 'feed-post-body-title'})

# Exibe o subtítulo no console
print(subtitulo.text)
