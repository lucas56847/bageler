import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def getinvasions(Coglist):

    url = "https://www.toonhq.org/invasions/"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(options = set_chrome_options())
    driver.get(url)

    page = driver.page_source
    i = 0
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')
    for container in soup.find_all('div', attrs={'class':'info-card__content'}):
     #   print(container.get_text(separator=" "))
        
        Coglist.append(container.get_text(separator="\n"))
   # for i in enumerate(Coglist):
       # Coglist[i] = "**" + Coglist[i]
      #  i = i+1
    print(Coglist)
    return(Coglist)