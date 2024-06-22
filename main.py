"""
Fetching data from prepared page and format it to the excel type file.
Combine of Selenium and BeautifulSoup
"""
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

PAGE_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORMS_URL = "https://forms.gle/rgDwthSDRGaKuEeE6"

response = requests.get(url=PAGE_URL)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.findAll(class_="PropertyCardWrapper__StyledPriceLine")
listing_link = soup.findAll(class_="StyledPropertyCardDataArea-anchor")
price_list = [item.get_text().split("+")[0] for item in price]
listing_list = [item.get_text().strip() for item in listing_link]
address_list = [item.get("href") for item in listing_link]
listing_list_formated = [item.replace(" |", "") for item in listing_list]

# forms part
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get(FORMS_URL)
time.sleep(2)
answer_input=driver.find_elements(By.CLASS_NAME,"zHQkBf")

answer_input[0].send_keys(address_list[0])
answer_input[1].send_keys(price_list[0])
answer_input[2].send_keys(listing_list_formated[0])

send_button=driver.find_element(By.CLASS_NAME,"Y5sE8d")
send_button.click()




