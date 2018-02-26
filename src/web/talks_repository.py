class TalkNotFoundException(Exception):
    pass


class TalksRepository:
    def __init__(self):
        self.talks = []

    def insert(self, talk):
        self.talks.append(talk)
        talk_id = len(self.talks) - 1
        return talk_id

    def get(self, talk_id):
        try:
            return self.talks[talk_id]
        except IndexError:
            raise TalkNotFoundException

    def delete(self, talk_id):
        try:
            del self.talks[talk_id]
        except IndexError:
            raise TalkNotFoundException
