from src.web.models.talk import Talks

class TalkNotFoundException(Exception):
    pass

class TalksRepository:
    def __init__(self):
        talk_repo = Talks()
        talk_repo.create_db()

    def insert(self, talk):
        talk_repo.add(talk.title, talk.duration)
        talk_repo.commit()
        self.talks.append(talk)
        talk_id = len(self.talks) - 1
        return talk_id

    def get(self, *talk_id):
        try:
            if talk_id:
                return self.talks[talk_id[0]]
            else:
                return self.talks
        except IndexError:
            raise TalkNotFoundException

    def delete(self, talk_id):
        try:
            del self.talks[talk_id]
        except IndexError:
            raise TalkNotFoundException
