import os
import random

from .texts import *


def create_random_object(all_vars):
    text = all_vars[random.randint(0, len(all_vars)-1)]
    random_object = list(text.values())
    return random_object


def get_city_and_state(path):
    with open(os.path.abspath('core/'+path), 'r', encoding='utf-8') as file:
        cities = file.readlines()

    for line in cities:
        line = line.replace('\n', '')
        city, state = line.split('\t')
        print(city+' - '+state)

    return cities


# get_city_and_state('cities.txt')

print(create_random_object(first_screen))
# create_random_object(second_screen)
# create_random_object(third_screen)
