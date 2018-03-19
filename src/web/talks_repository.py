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
        print('into get', talk_id)
        try:
            if type(talk_id) is int:
                print('I have id')
                return self.talks[talk_id]
            else:
                print('I dont have id')
                return self.talks
        except IndexError:
            raise TalkNotFoundException

    def delete(self, talk_id):
        try:
            del self.talks[talk_id]
        except IndexError:
            raise TalkNotFoundException
