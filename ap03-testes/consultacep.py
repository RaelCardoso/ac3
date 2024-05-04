from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

site = "https://buscacepinter.correios.com.br/app/endereco/index.php"
browser.get(site)

time.sleep(3)

cep = "09390360"

browser.find_element(By.NAME, 'endereco').send_keys(cep)

time.sleep(3)

browser.find_element(By.NAME, 'btn_pesquisar').click()

time.sleep(4)
# retirando a informacao do endereco
endereco = browser.find_element(By.XPATH, "/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]").text
bairro = browser.find_element(By.XPATH, "/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[2]").text
cidade = browser.find_element(By.XPATH, "/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[3]").text

time.sleep(2)

browser.quit()

resultado_final = endereco + '\n' + bairro + '\n' + cidade
print(resultado_final)
