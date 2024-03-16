import requests
from bs4 import BeautifulSoup

class Screaping:
    def screaping(self):
        headers = {
            'User-Agent'        : 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
            'Accept'            : '*/*',
            'Accept-Language'   : 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'DNT'               : '1',
            'Connection'        : 'close'
        } 

        link = 'https://www.fundamentus.com.br/resultado.php'
        try:
            requisicao = requests.get(link, headers=headers, timeout=5).text
            soup = BeautifulSoup(requisicao, "html.parser")
            table = soup.find('table')

            print(table)
            
            return table
        except RecursionError:
            print("\nFalha na Requisição\n")
            return ""
        
if __name__=="__main__":
    Screaping().screaping()