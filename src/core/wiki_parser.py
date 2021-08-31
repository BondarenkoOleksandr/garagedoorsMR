import re

from bs4 import BeautifulSoup
import urllib.request


def remove_html_tags(data):
    p = re.compile(r'\[.*?\]|<.*?>')
    return p.sub('', data)


def parse_wiki(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    data = [data.replace('\n', '') for data in data]
    cleaned_data = []
    for elem in data:
        parser = 'html.parser'
        resp = urllib.request.urlopen("https://en.m.wikipedia.org/wiki/" + elem.replace(' ', '_'))
        soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

        indx = 0
        for p in soup.find_all('p'):
            indx += 1
            if indx == 2:
                cleaned_data.append(remove_html_tags(str(p)).strip())
                break

    return cleaned_data
