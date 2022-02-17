import requests
from bs4 import BeautifulSoup
from data.config import *


def news_parser():
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    all_news = soup.findAll("a", class_="list-item__title color-font-hover-only", href=True)
    sl = {}
    for data in all_news:
        name_of_new, link = data.text, data["href"]
        one_time_page = requests.get(link)
        one_time_soup = BeautifulSoup(one_time_page.text, "html.parser")
        one_time_parser = one_time_soup.findAll("div", class_="article__block")
        text = ""
        for one_time_data in one_time_parser:
            text += one_time_data.text + " "
        sl[data.text] = text
    return sl
