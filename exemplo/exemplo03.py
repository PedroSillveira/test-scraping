from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get('https://www.walissonsilva.com/blog')
elemento = navegador.find_element(By.TAG_NAME, 'input')
elemento.send_keys('python') # pesquisa o conteudo solicitado no elemento <input> da pagina

input("Pressione Enter para fechar o navegador...")
