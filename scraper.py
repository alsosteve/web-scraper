import requests
from bs4 import BeautifulSoup
import re

URL = "https://en.wikipedia.org/wiki/Taco"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")


def get_citations_needed_report():
    for p in results:
        tag = p.parent.parent.parent
        tag = str(tag)
        regex = r"<[^<>]+>"
        data =  re.sub(regex, '', tag)
        print(data)

def get_citations_needed_count():
    count = 0
    for p in results:
        count += 1
    print(count)

get_citations_needed_count()       
get_citations_needed_report()