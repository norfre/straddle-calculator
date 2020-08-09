import requests
import time
from bs4 import BeautifulSoup
import re

url1 = 'https://classic.nordnet.se/mux/web/marknaden/aktiehemsidan/warranter.html?market_view=&instr_group_type=WOKO&instr_type=&issuer=&date=&identifier='
url2 = '&marketplace=11&selectedtab=Overview&marknad=SE&instrument=101_11_&sortcolumn=shortname&sortorder=ascending'
identifier = '366'

url = url1 + identifier + url2

response = requests.get(url)

print(response) # 200 means OK

soup = BeautifulSoup(response.text, "html.parser")

warrants = soup.find_all("td", string=re.compile(".warrant"))

for warrant in warrants:
    print(warrant.string)
    b = warrant.find_previous_sibling("td")
    print(b.string)
    c = warrant.find_next_siblings("td")
    for line in c:
        print(line.string)

time.sleep(1)

underlying = soup.find("a", class_=("underline"))
print(underlying.string)
parent = underlying.find_parent()
siblings = parent.find_next_siblings("td")
for sibling in siblings:
    print(sibling.string)
