from selenium                          import webdriver
from selenium.webdriver.common.by      import By
from webdriver_manager.chrome          import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait   import WebDriverWait
from crud                              import crud

class scraping:
    __obj_crud = None
    def __init__(self):
        self.__obj_crud = crud()     

    def switch(self, case, campeonato):
        if case == 'times':
            if campeonato == 'premier':            
                return self.timesPremier()
            else:
                print("campeonato invalido")
        elif case == 'rodadas':
            if campeonato == 'premier':  
                return self.rodadasPremier()
            else:
                print("campeonato invalido")
        else:
            print("metódo invalido")


    def timesPremier(self):
        servico = Service(ChromeDriverManager().install())
        url = "https://www.sofascore.com/tournament/football/england/premier-league/17#52186"   

        navegador = webdriver.Chrome(service=servico)
        WebDriverWait(navegador, timeout=10)
        navegador.get(url)

        click = navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[1]/div/div[1]/div/h2[3]')
        click.click()

        # TEMPO DE ESPERA PARA DISPARA AÇÃO
        navegador.implicitly_wait(20)

        dados = navegador.find_elements(By.CLASS_NAME, 'uTWnT')     
        if(dados):
            time = []
            temporada = '2023/2024'
            for dado in dados:
                if dado.text and dado.text != '0':
                    time.append(dado.text)
        else:
            print("Sem dados")        
        
        for t1 in time:
            print(t1)           
            # self.__obj_crud.inserir(t1,temporada)


                   
    def rodadasPremier(self):
        servico = Service(ChromeDriverManager().install())
        url = "https://www.sofascore.com/tournament/football/england/premier-league/17#52186"   

        navegador = webdriver.Chrome(service=servico)
        WebDriverWait(navegador, timeout=10)
        navegador.get(url)

       
        click = navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[1]/div/div[1]/div/h2[2]')
        click.click()

        # TEMPO DE ESPERA PARA DISPARA AÇÃO
        navegador.implicitly_wait(20)
        
        click2 = navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]')
        click2.click()

        # TEMPO DE ESPERA PARA DISPARA AÇÃO
        navegador.implicitly_wait(20)
      
        click3 = navegador.find_element(By.XPATH, '//*[@id="downshift-11-toggle-button"]')
        click3.click()

        # TEMPO DE ESPERA PARA DISPARA AÇÃO
        navegador.implicitly_wait(20)
              
        click4 = navegador.find_element(By.XPATH, '//*[@id="downshift-11-item-0"]')
        click4.click()
       
        list = {}
        dados = navegador.find_elements(By.CLASS_NAME, 'bwUmPO') 
        contador = 0
        for dado in dados:                
            contador += 1
            div = contador % 2     
             
            if div == 1:                
                list[contador]               = {'rodada':'1'}
                list[contador]['campeonato'] = 'premier league'
                list[contador]['mandante']   = dado.text
            else:                
                cont = contador - 1                
                list[cont]['visitante']   = dado.text
               
        
        self.__obj_crud.newInsert(list)        
           


scrap = scraping() 
scrap.switch('rodadas','premier')



    