###Cria bloco de sessões para ser adicionadas as palestras;
"""
Há dois blocos de sessões: manhã e tarde.
Sessão da manhã se inicia as 9h;
Sessão da tarde se inicia as 13h;
A sessão da tarde deve ser finalizada entre 16h e 17h a tempo
de se realizar o evento de network.
Os apresentadores são pontuais, sem espaço entre as palestras.
"""
from datetime import timedelta

class ScheduledTalk:
    def __init__(self, talk, date):
        self.talk = talk
        self.date = date


class NoEnoughtSpace(Exception):
    pass


class Track:
    def __init__(self, date):
        self.next_date = date.replace(hour=9, minute=0, second=0, microsecond=0)
        self.scheduled_talks = []

    def schedule_talk(self, talk):
        scheduled = ScheduledTalk(talk, self.next_date)
        self.scheduled_talks.append(scheduled)
        self.next_date = self.next_date + timedelta(minutes=talk.duration)
