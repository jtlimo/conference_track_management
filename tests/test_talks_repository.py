from web.talks_repository import TalksRepository
from src.talk import Talk


class TestTalksRepository:

    def test_insertion_talk(self):
        talk = Talk("Luna", 60)
        repo = TalksRepository()

        talk_inserted = repo.insert(talk)

        assert inserted_talk.title == talk.title
        assert inserted_talk.duration == talk.duration
