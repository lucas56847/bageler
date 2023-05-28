import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.toonhq.org/invasions/"
options = Options()
options.add_argument('--headless')
#options.add_argument('--disable-gpu')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')



for container in soup.find_all('div', attrs={'class':'info-card__title'}):
    print(container.get_text(separator=" "))