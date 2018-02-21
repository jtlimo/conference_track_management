from web.talks_repository import TalksRepository
from src.talk import Talk


class TestTalksRepository:

    def test_insertion_talk(self):
        talk = Talk("Luna", 60)
        repo = TalksRepository()

        id_talk = repo.insert(talk)

        assert id_talk == 0

    def test_get_talk_by_id(self):
        talk = Talk("Biancat", 30)
        repo = TalksRepository()

        id_talk = repo.insert(talk)

        assert repo.get(id_talk).title == talk.title
        assert repo.get(id_talk).duration == talk.duration
