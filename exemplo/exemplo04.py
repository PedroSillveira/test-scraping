import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from time import sleep

# Configurações do navegador
options = Options()
options.add_argument('window-size=1200,800')  # Tamanho maior para evitar problemas de renderização
# options.add_argument('--headless')  # Executa sem abrir o navegador (descomente se necessário)

# Inicializa o navegador Chrome com as opções configuradas
navegador = webdriver.Chrome(options=options)

# Abre o site do Airbnb
navegador.get('https://www.airbnb.com.br')

# Aguarda um tempo para garantir que a página carregue completamente
sleep(3)

# 🔎 Encontra o campo de pesquisa pelo seletor correto
try:
    input_place = navegador.find_element(By.XPATH, "//input[@placeholder='Buscar destinos']")
    input_place.click()  # Clica no campo para ativá-lo
    sleep(1)  # Pequena pausa para evitar bugs
    input_place.send_keys('São Paulo')  # Digita o nome da cidade
    sleep(1)
    input_place.send_keys(Keys.RETURN)  # Pressiona Enter para buscar
except Exception as e:
    print("Erro ao encontrar o campo de busca:", e)
    navegador.quit()
    exit()

# Aguarda alguns segundos para os resultados carregarem
sleep(5)

# Extrai o HTML da página carregada pelo Selenium
site = BeautifulSoup(navegador.page_source, 'html.parser')

# 🖥️ Exibe um trecho do HTML para verificar se os resultados foram carregados
print(site.prettify()[:1000])  # Apenas os primeiros 1000 caracteres para verificação

# Mantém a página aberta até que o usuário pressione Enter
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador ao final
navegador.quit()
