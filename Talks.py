from datetime import datetime, timedelta

#classe que cria e valida as talks;
"""
A duração das palestras devem ser em minutos;
A duração da menor palestra será as lightnings que são de 5 minutos.
O título das palestras não contém números.
Os apresentadores são pontuais, sem espaço entre as palestras.
"""

class Talks:

    def __init__(self, duration, title):
        self.duration = duration
        self.title = title

    def create_talk(duration, title):
        get_a_time_to_talk(duration)


    def get_a_time_to_talk(duration):
        actual_time = datetime.now()
        time_of_talk = actual_time - timedelta(minutes=duration)
        return time_of_talk.strftime("%I:%M%p") , time_of_talk
