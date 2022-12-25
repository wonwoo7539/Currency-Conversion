import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    respons = requests.get("https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_{}{}".format(target1, target2), headers=headers)
    content = BeautifulSoup(respons.content, 'html.parser')
    containers = content.find('p', {'class': 'no_today'})
    print(containers.text)

get_exchange_rate('usd', 'eur')