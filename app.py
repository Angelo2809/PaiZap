from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import functions

wpp = 'https://web.whatsapp.com/'

options = Options()
options.add_argument("start-maximized")
options.add_argument(r"user-data-dir=C:\Users\Angelo\AppData\Local\Google\Chrome\User Data")
navegador = webdriver.Chrome(executable_path = 'chromedriver.exe', options=options)
navegador.get(wpp)
time.sleep(20)
chat = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]").click()
print("Chat iniciado")
time.sleep(2)
qtd_mensagem = len(navegador.find_elements(By.CLASS_NAME, "hY_ET"))
ultima_mensagem = navegador.find_elements(By.CLASS_NAME, "hY_ET")[-1].text
loops = 0
while True:
    time.sleep(5)
    print(50*'-')
    print(f'Loop: {loops}')

    mensagem = navegador.find_elements(By.CLASS_NAME, "hY_ET")[-1].text
    # for m in mensagem:
    #     print(m.text)
    print(mensagem, "\n*\n" , ultima_mensagem)
    
    if mensagem != ultima_mensagem:
        
        print(50*'-')
        print("Nova mensagem")
        print(mensagem)
        print(50*"-")

        try:
            campo_escrita = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p")
        except:
            campo_escrita = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]")
        campo_escrita.clear()
        #resp = "TO AQUI"
        resp = functions.chat(mensagem)
        campo_escrita.send_keys(resp)
        #enviar = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span").click()
        ultima_mensagem = resp.strip()
    loops += 1 
