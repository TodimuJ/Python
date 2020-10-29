import json
import re
import requests
from bs4 import BeautifulSoup 

'''Track lowest prices'''

URL = 'Enter URL'

headers = {
            "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
            }

def check_price():
    request = requests.get(URL, headers = headers)

    test = BeautifulSoup(request.content, 'html.parser')

    looking = test.find(itemprop="name").get_text().strip()

    price = test.find("div", {"class": "ProductPrice"}).get_text().strip()
    converted_price = float(re.findall(r'\b\d+\b', price)[0])

    # if (converted_price < 60):
    #     send_mail()

    print(looking)
    print(converted_price)

#def send_mail()