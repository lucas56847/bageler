import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#TODO you gottta fix the errors to improve runtime -- done?

#defines arguments for webdriver which is run by selenium
def getinvasions(Coglist):

    url = "https://www.toonhq.org/invasions/"
    options = Options()
    options.add_argument("enable-automation")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.get(url)

    page = driver.page_source
    i = 0
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')
    
    #TODO Formatting?? Probably just some bold text around the cog name but you never know. Likely not
    #necessary to include labels unless you include an approximately around the time - 
    
    for container in soup.find_all('div', attrs={'class':'info-card__content'}):
     #   print(container.get_text(separator=" "))
        
        Coglist.append(container.get_text(separator="\n"))
        
    for i in range(len(Coglist)):
        Coglist[i] = "**" + Coglist[i]
        Coglist[i] = Coglist[i].replace("\n","**\n",1)
        
    print((Coglist))
    return(Coglist)