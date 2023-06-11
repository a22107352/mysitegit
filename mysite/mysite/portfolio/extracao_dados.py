import requests
from bs4 import BeautifulSoup
import os

from bs4 import BeautifulSoup
import requests
import csv


def extrai_info_de_url(url):
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        anos = soup.find('div', class_='YearCurrentText')
        obitos = soup.find('div', class_='ValueText')
        return {'anos': anos.text, 'obitos': obitos.text}
    else:
        return None


url = 'https://www.pordata.pt/portugal/obitos+de+residentes+em+portugal+total+e+no+primeiro+ano+de+vida-15'
extrai_info_de_url(url)
