import os
import random
import re

from bs4 import BeautifulSoup
import urllib.request


def remove_html_tags(data):
    p = re.compile(r'\[.*?\]|<.*?>')
    return p.sub('', data)


def parse_wiki(path):
    with open(os.path.abspath('src/core/' + path), 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # data = []
    # for el in lines:
    #     data.append(el.replace('\n', '').split('\t'))
    #     temp_el = el.replace('\n', '').split('\t')
    #     with open('new_cities.txt', 'a', encoding='utf-8') as f:
    #         try:
    #             f.write(temp_el[0]+'||'+temp_el[1]+'\n')
    #         except:
    #             f.write(temp_el[0]+'Error')

    data = [elem.replace('\n', '').split('||') for elem in lines]

    cleaned_data = {}
    for elem in data:
        parser = 'html.parser'
        link = "https://en.m.wikipedia.org/wiki/" + elem[0].replace(' ', '_') + ',_' + elem[1].replace(' ', '_')
        resp = urllib.request.urlopen(link)
        # resp = urllib.request.urlopen("https://en.m.wikipedia.org/wiki/" + elem[0].replace(' ', '_'))
        soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

        indx = 0
        for p in soup.find_all('p'):
            indx += 1
            if indx == 2:
                cleaned_data.update({elem[0]: remove_html_tags(str(p)).strip()})
                break

    return cleaned_data


def get_data_names(path):
    with open(os.path.abspath('src/core/' + path), 'r', encoding='utf-8') as f:
        data = f.readlines()

    data_names = [data.replace('\n', '').split('||') for data in data]

    return data_names


def create_random_object(all_vars):
    random_object = all_vars[random.randint(0, len(all_vars) - 1)]
    return random_object


def replace_test_name(name, data):
    for key, value in data.items():
        data[key] = data[key].replace(' Test', ' ' + name)

    return data
