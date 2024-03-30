import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import SessionNotCreatedException
#use selenium 4.8.3
#TODO you gottta fix the errors to improve runtime -- done?

class driverError(Exception):
    pass

#defines arguments for webdriver which is run by selenium
def getinvasions(Coglist):

    url = "https://www.toonhq.org/invasions/"
    options = Options()
    options.add_argument("enable-automation")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        if driver == None:
            raise driverError
        driver.get(url)

        page = driver.page_source
        driver.quit()
        
    except SessionNotCreatedException:
        errorStr = 1
        print("Ruh roh!")
        return(errorStr)
    except:
        errorStr = 2
        print("Zoinks!")
        return(errorStr)
    else:
        soup = BeautifulSoup(page, 'html.parser')
    
        for container in soup.find_all('div', attrs={'class':'info-card__content'}):       
            Coglist.append(container.get_text(separator="\n"))
        i = 0
        
        for i in range(len(Coglist)):
            Coglist[i] = "**" + Coglist[i]
            Coglist[i] = Coglist[i].replace("\n","**\n",1)
        
    print(Coglist)
    print("Returning successfully")
    return(Coglist)