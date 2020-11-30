from bs4 import BeautifulSoup
import requests

class Parse():
    def __init__(self, url):
        self.url = url
        self.compliments = []   #here compliments will contain 
        source = requests.get(url)  #get site
        self.html = BeautifulSoup(source.text, 'lxml')

    def get_content(self):  #find complimets and append it in compliments[]
        bs_compliments = self.html.find('div', {'class':'site-content-inner'})    
        for a in bs_compliments.find_all('span', {'itemprop':'headline'}):
            links = a.find_all('a')
            for value in a:
                if value.text != "":
                    self.compliments.append(value.text)
            

        return self.compliments
        