import DbConnect
import Logger
import Scraper
class MainWorking:
    LinksList=[]
    dbConnect =None
    my_logger = Logger.get_logger("myProgram")
    def LoadLinks(self):
        with open('E:\\Working Programs\\scrap\\Linkuri.txt') as f:
            self.LinksList = f.readlines()

    def ConnectDatabase(self):
        self.DbConnect = DbConnect.DbConnect(self.my_logger)

    def CreateScrapper(self):
        self.Scraper=Scraper.Scraper(self.DbConnect,self.my_logger)

    def Work(self):
        self.LoadLinks()
        self.ConnectDatabase()
        self.CreateScrapper()
        for link in self.LinksList:
            if "emag" in link:
                try:
                    self.Scraper.start_scrap_Emag(link)
                    self.my_logger.info("Link Rezolvat "+link)
                except Exception as ex:
                    self.my_logger.error(ex)

            else:
                self.my_logger.error("Link neidentificat "+link)


worker=MainWorking()
worker.Work()




