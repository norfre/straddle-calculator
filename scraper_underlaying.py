import requests
import time
from bs4 import BeautifulSoup
import re

'''
This is to find available underlying instrumets
'''

url = 'https://www.avanza.se/borshandlade-produkter/warranter-torg/lista.html?name=&warrantTypes=PLAIN_VANILLA&sortField=TOTAL_VALUE_TRADED&sortOrder=DESCENDING'

response = requests.get(url)

print(response) # 200 means OK

soup = BeautifulSoup(response.text, "html.parser")
underlyings = soup.find(id="underlyingInstrument")

for underlying in underlyings:
    if len(underlying.string) < 2:
        continue
    else:
        print(underlying.string)
