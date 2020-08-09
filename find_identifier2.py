import requests
import time
from bs4 import BeautifulSoup
import re

url = 'https://classic.nordnet.se/mux/web/marknaden/kurslista/aktier.html'

response = requests.get(url)

print(response) # 200 means OK

soup = BeautifulSoup(response.text, "html.parser")

underlyings = soup.find_all("a", class_='underline')

for underlying in underlyings:

    print(underlying.string)

    href = underlying.get('href')
    string = href.split('=')[1].split('&')
    identifier = string[0]
    print(identifier)
