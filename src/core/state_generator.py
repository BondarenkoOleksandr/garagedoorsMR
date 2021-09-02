from core.generator import parse_wiki, get_data_names, create_random_object, replace_test_name
from states.models import State, FirstScreen, SecondScreen, ThirdScreen
from .texts import *

def generate():
    states_descr = parse_wiki('states.txt')
    states_names = get_data_names('states.txt')
    for name in states_names:
        State.objects.create(
            name=name,
            description=states_descr[name]
        )
        state = State.objects.filter(name=name).first()

        first_screen_text = create_random_object(first_screen)
        FirstScreen.objects.create(
            state=state,
            title=first_screen_text['title'].replace(' Test', ' '+name),
            description=first_screen_text['descr'].replace(' Test', ' '+name),
        )

        second_screen_text = create_random_object(second_screen)
        SecondScreen.objects.create(
            state=state,
            main_title=second_screen_text['scf_title'].replace(' Test', ' '+name),
            main_description=second_screen_text['scf_text'].replace(' Test', ' '+name),
            sec_title=second_screen_text['scs_title'].replace(' Test', ' '+name),
            sec_description=second_screen_text['scs_text'].replace(' Test', ' '+name)
        )

        third_screen_text = create_random_object(third_screen)
        ThirdScreen.objects.create(
            state=state,
            main_title=third_screen_text['services_title'].replace(' Test', ' '+name),
            main_description=third_screen_text['services_text'].replace(' Test', ' '+name),
            sec_title=third_screen_text['services_smf_ttl'].replace(' Test', ' '+name),
            sec_description=third_screen_text['services_smf_txt'].replace(' Test', ' '+name),
            thrd_title=third_screen_text['services_sms_ttl'].replace(' Test', ' '+name),
            thrd_description=third_screen_text['services_sms_txt'].replace(' Test', ' '+name)
        )
