from selenium import webdriver
# Importa o Selenium para controlar o navegador
from selenium.webdriver.common.by import By
# Importa métodos para localizar elementos na página

# Inicializa o navegador Chrome
navegador = webdriver.Chrome()
# Acessa a página desejada
navegador.get('https://www.walissonsilva.com/blog')
# Encontra o primeiro elemento <input> da página
elemento = navegador.find_element(By.TAG_NAME, 'input')
# Envia o texto "data" para o campo de entrada <input>
elemento.send_keys('data')
