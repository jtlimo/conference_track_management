from web.talks_repository import TalksRepository
from src.talk import Talk


class TestTalksRepository:

    def test_insertion_talk(self):
        talk = Talk("Luna", 60)
        repo = TalksRepository()

        talk_inserted = repo.insert(talk)

        assert talk_inserted[0].title == talk.title
        assert talk_inserted[0].duration == talk.duration
