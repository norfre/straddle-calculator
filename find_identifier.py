import requests
import time
from bs4 import BeautifulSoup
import re

'''
This is to translate naming from Avanza to Nordnet
'''

url1 = 'https://www.nordnet.se/marknaden/warrant-listor?freeTextSearch='
url2 = 'VOLVO%20B'
url = url1 + url2

response = requests.get(url)

print(response) # 200 means OK

soup = BeautifulSoup(response.text, "html.parser")

underlyings = soup.find_all("a", href=re.compile("/marknaden/aktiekurser/."))
print(underlyings[2].string)
