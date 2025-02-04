import requests  
# Biblioteca para fazer requisições HTTP
from bs4 import BeautifulSoup  
# Biblioteca para processar HTML


# URL base do Mercado Livre para busca de produtos
url_base = 'https://lista.mercadolivre.com.br/'
# Solicita ao usuário o nome do produto a ser pesquisado
produto_pesquisa = input('Qual produto deseja? ')


# Define um cabeçalho User-Agent para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


# Faz uma requisição para a página de pesquisa do Mercado Livre com o produto desejado
response = requests.get(url_base + produto_pesquisa, headers=headers)
# Converte o conteúdo da resposta para HTML usando BeautifulSoup
site = BeautifulSoup(response.text, 'html.parser')


# Encontra o primeiro item da lista de produtos na página
produto = site.find('div', attrs={'class': 'poly-card poly-card--list'})
# Obtém o título do produto
titulo = produto.find('h3', attrs={'class': 'poly-component__title-wrapper'})
# Obtém o link para a página do produto
link = produto.find('a', attrs={'class': 'poly-component__title'})
# Obtém o preço do produto
price = produto.find('div', attrs={'class': 'poly-price__current'})


# Utiliza a função prettify para exibir o HTML de forma mais legível (ajuda na depuração)
print(produto.prettify())
# Exibe o título do produto
print(titulo.text)
# Exibe o link para o produto
print(link['href'])
# Exibe o preço do produto
print(price.text)