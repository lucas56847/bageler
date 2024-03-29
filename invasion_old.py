import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getinvasions(Coglist):

    url = "https://www.toonhq.org/invasions/"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    page = driver.page_source
   # Coglist =[]
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')
    for container in soup.find_all('div', attrs={'class':'info-card__title'}):
        print(container.get_text(separator=" "))
        Coglist.append(container.get_text(separator="\n"))
    return(Coglist)