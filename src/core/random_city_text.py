import random

from texts import *


def create_random_city(all_vars):
    text = all_vars[random.randint(0, len(all_vars)-1)]
    val = list(text.values())
    print(val)


def get_city_and_state(path):
    with open(path, 'r', encoding='utf-8') as file:
        cities = file.readlines()

    for line in cities:
        line = line.replace('\n', '')
        city, state = line.split('\t')
        print(city+' - '+state)

    return cities



cities = get_city_and_state('cities.txt')

# create_random_city(first_screen)
# create_random_city(second_screen)
# create_random_city(third_screen)
