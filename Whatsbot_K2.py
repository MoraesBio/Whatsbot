#Importar o pandas para importar os dados da tabela de contatos
import pandas as pd
import time
import urllib.parse

#ler a lista de contatos
contatos = pd.read_excel("Contato.xlsx")
print(contatos)

#Importar o Selenium
from selenium import webdriver #Abrir o navegador
from selenium.webdriver.common.keys import Keys #Permite enviar a mensagem para as pessoas
from selenium.webdriver.common.by import By

#Abrindo a aba do Navegador
navegador = webdriver.Chrome() #Webdriver permite a comunicação do Python com o navegador

#Indo até o site do whatsapp web
navegador.get("http://web.whatsapp.com/")

#Identificar que o whatsapp já abriu na página
while len(navegador.find_elements(by=By.ID, value="side")) < 1:
    time.sleep(1)

from datetime import datetime
hora = datetime.now().time()
hora_atual = hora.strftime('%H:%M')
#print(hora_atual)

#Já estamos logados no whatsapp web
while int(hora.strftime('%H')) > 8 and int(hora.strftime('%H')) < 18:
# print(hora_atual)

    for i, mensagem in enumerate(contatos['Mensagem']):
        pessoa = contatos.loc[i, "Pessoa"]
        numero = contatos.loc[i, "Número"]

        #Devemos agora enviar a mensagem
        texto = urllib.parse.quote(f"{mensagem}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)

        while len(navegador.find_elements(By.ID, "side")) < 1:
            time.sleep(5)
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(10)