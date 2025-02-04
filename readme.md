# 🕷️ Projeto de Scraping do G1 e Mercado Livre  

Este projeto realiza **web scraping** em dois sites:  
- **G1**.  
- **Mercado Livre**.  

O objetivo é aprender os conceitos básicos de scraping utilizando **Python**, com as bibliotecas `requests` e `BeautifulSoup`.

## 🚀 Tecnologias Utilizadas  

- **Python**  
- **Requests** – Para fazer requisições HTTP.  
- **BeautifulSoup4** – Para processar e extrair informações do HTML.  

## 📌 Funcionalidades  

🔹 Scraping do G1  
- Obtém o título e subtítulo da notícia principal da página inicial do G1.  

 🔹 Scraping do Mercado Livre  
- Permite que o usuário pesquise um produto.  
- Coleta título, link e preço dos produtos encontrados.  
- Exibe os resultados organizadamente.  

## 🛠️ Instalação  

Clone este repositório:  

```bash
git clone https://github.com/seu-usuario/projeto-scraping.git
cd projeto-scraping
```

Instale as dependências:  

```bash
pip install requests beautifulsoup4
```

## ▶️ Como Usar  

Scraping do G1:  

```bash
python scraping_g1.py
```

Scraping do Mercado Livre:  

```bash
python scraping_mercadolivre.py
```

## ⚠️ Observações  

- O **User-Agent** foi incluído para evitar bloqueios em algumas páginas.  
- Os sites podem mudar sua estrutura, exigindo ajustes no código.  