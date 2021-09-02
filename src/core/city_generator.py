from core.generator import parse_wiki, get_data_names, create_random_object, replace_test_name
from cities.models import City, FirstScreen, SecondScreen, ThirdScreen
from states.models import State
from .texts import *


def generate():
    cities_descr = parse_wiki('new_cities.txt')
    cities_names = get_data_names('new_cities.txt')

    for name in cities_names:
        state = State.objects.filter(name=name[1]).first()
        if name[0] in cities_descr.keys():
            city = City.objects.create(
                state=state,
                name=name[0],
                description=cities_descr[name[0]]
            )
        else:
            city = City.objects.create(
                state=state,
                name=name[0],
                description='will be soon'
            )

        first_screen_text = create_random_object(first_screen)
        FirstScreen.objects.create(
            city=city,
            title=first_screen_text['title'].replace(' Test', ' ' + name[0]),
            description=first_screen_text['descr'].replace(' Test', ' ' + name[0]),
        )

        second_screen_text = create_random_object(second_screen)
        SecondScreen.objects.create(
            city=city,
            main_title=second_screen_text['scf_title'].replace(' Test', ' ' + name[0]),
            main_description=second_screen_text['scf_text'].replace(' Test', ' ' + name[0]),
            sec_title=second_screen_text['scs_title'].replace(' Test', ' ' + name[0]),
            sec_description=second_screen_text['scs_text'].replace(' Test', ' ' + name[0])
        )

        third_screen_text = create_random_object(third_screen)
        ThirdScreen.objects.create(
            city=city,
            main_title=third_screen_text['services_title'].replace(' Test', ' ' + name[0]),
            main_description=third_screen_text['services_text'].replace(' Test', ' ' + name[0]),
            sec_title=third_screen_text['services_smf_ttl'].replace(' Test', ' ' + name[0]),
            sec_description=third_screen_text['services_smf_txt'].replace(' Test', ' ' + name[0]),
            thrd_title=third_screen_text['services_sms_ttl'].replace(' Test', ' ' + name[0]),
            thrd_description=third_screen_text['services_sms_txt'].replace(' Test', ' ' + name[0])
        )
