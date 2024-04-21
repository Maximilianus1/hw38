from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
def getInfo(url):
    driver.get(url)
    info = driver.find_elements(By.XPATH,'//div[@class="price"]//span')
    try:
        for i in range(len(info)):
            print(info[i].text)
    except:
        print('nothing')
url = "https://www.flip.kz/"
getInfo(url)
