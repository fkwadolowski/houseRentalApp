"""
Fetching data from prepared page and format it to the excel type file.
Combine of Selenium and BeautifulSoup
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


PAGE_URL="https://appbrewery.github.io/Zillow-Clone/"
FORMS_URL="https://forms.gle/hjZuyYGwVT55D389A"

response=requests.get(url=PAGE_URL)
soup= BeautifulSoup(response.text, "html.parser")
price=soup.findAll(class_="PropertyCardWrapper__StyledPriceLine")
listing_link=soup.findAll(class_="StyledPropertyCardDataArea-anchor")
price_list=[item.get_text().split("+")[0] for item in price]
listing_list=[item.get_text().strip() for item in listing_link]
address_list=[item.get("href") for item in listing_link]
print("first:",listing_list)
listing_list_fromated=[item.replace(" |","") for item in listing_list]
print("second:",listing_list_fromated)
  # forms part



