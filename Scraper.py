from urllib.request import urlopen as uReq
import urllib
from bs4 import BeautifulSoup as soup
from requests import get
import DbConnect
import Logger
import re
class Scraper:
    dbConnect = None
    def __init__(self,dbConnect,my_logger):
        #self.dbConnect=dbConnect
        pass
        #self.my_logger = my_logger

    def start_scrap_Emag(self,page_url):
        try:

            uClient = uReq(page_url)

            # parses html into a soup data structure to traverse html
            # as if it were a json data type.
            page_soup = soup(uClient.read(), "html.parser")
            uClient.close()
            containers = page_soup.findAll("p", {"class": "product-new-price"})
            Price = containers[0].text.strip()
            pr=Price.split(' ')
            pret=pr[0]
            pret=pret[:-2]


            containers = page_soup.findAll("h1", {"class": "page-title"})
            Title = containers[0].text.strip()
            Object=Title.split(',')

            containers = page_soup.findAll("p", {"class": "product-old-price"})
            PriceOld = containers[0].text.strip()
            self.dbConnect.InsertPrice(Object[0],pret,page_url)
        except Exception as ex:
            pass
            #self.my_logger.error(ex)

    def start_scrap_Autovit(self):
        try:
            # merge asa. ajungi la tot tagul care contine poza
            # sunt poze mici dar pot fi redimensionate daca le schimbi de url marimea
            # date despre masina se regaseste in page_soup

            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Referer': 'https://cssspritegenerator.com',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}


            d = get("https://www.autovit.ro/anunt/skoda-octavia-ID7GAtiU.html#7ce9f71ee3", headers=hdr)
            #uClient = uReq("https://www.autovit.ro/anunt/skoda-octavia-ID7GAtiU.html#7ce9f71ee3")

            # parses html into a soup data structure to traverse html
            # as if it were a json data type.
            page_soup = soup(d.content, "html.parser")
            #uClient.close()
            containers = page_soup.findAll("div", {"class": "photo-item"})
            Price = containers[0].text.strip()
            pr = Price.split(' ')
            pret = pr[0]
            pret = pret[:-2]

            containers = page_soup.findAll("h1", {"class": "page-title"})
            Title = containers[0].text.strip()
            Object = Title.split(',')

            containers = page_soup.findAll("p", {"class": "product-old-price"})
            PriceOld = containers[0].text.strip()
            #self.dbConnect.InsertPrice(Object[0], pret, https://www.autovit.ro/anunt/bmw-seria-3-320-ID7GAnKZ.html)
        except Exception as ex:
            pass
            #self.my_logger.error(ex)


aa=Scraper('a','a')
aa.start_scrap_Autovit()



