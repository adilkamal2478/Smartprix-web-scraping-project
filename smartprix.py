from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

s = Service("C:/Users/adilk/OneDrive/Desktop/chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=s , options=options)

driver.get("https://www.smartprix.com/mobiles")
time.sleep(2)

driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(5)
driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(5)


old_height = driver.execute_script("return document.body.scrollHeight")
count = 1
while True:
    driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/div[1]/div[2]/div/div[3]').click()
    time.sleep(5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(4)

    print(count)
    count += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break
    old_height = new_height


html = driver.page_source
with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)