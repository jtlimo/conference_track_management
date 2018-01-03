import re
from datetime import datetime, timedelta

#classe que cria e valida as talks;
"""
A duração das palestras devem ser em minutos;
A duração da menor palestra será as lightnings que são de 5 minutos.
O título das palestras não contém números.
"""

class Talks:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def create_talk(title, duration):
        ##Pq tenho que colocar Talks.funcao?!?
        if Talks.check_title_contains_numbers(title) > 0:
            raise ValueError
        else:
            return {'title': title, 'time_of_talk': Talks.get_a_time_to_talk(duration)}

    def get_a_time_to_talk(duration):
        actual_time = datetime.now()
        time_of_talk = actual_time - timedelta(minutes=duration)
        return time_of_talk.strftime("%I:%M%p") , time_of_talk

    def check_title_contains_numbers(title):
        regex_pattern = r'[\d]'
        return len(re.findall(regex_pattern, title))
