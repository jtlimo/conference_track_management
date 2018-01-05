import pytest
from Talks import Talks
from datetime import datetime, date, time, timedelta

class TestTalkValidations(object):

    @pytest.mark.test
    def test_isminutetalk(self, time=60, track_title="track title example"):

        talk = Talks(track_title, time).create_talk()

        print(talk)
        new_time = talk['time_of_talk']['timedelta'] - timedelta(minutes=time)

        expected_time = new_time + timedelta(minutes=time)

        assert talk['time_of_talk']['timedelta'], expected_time

    #input Writing Fast Tests Against Enterprise Rails 60min
    #output 09:00AM Writing Fast Tests Against Enterprise Rails 60min
    def test_title_talk(self, title="Writing Fast Tests Against Enterprise Rails", time=60):

        talk = Talks(title, time).create_talk()

        assert title == talk['title']

    def test_title_not_contain_numbers(self, title="Writing blabla5325", time=60):

        with pytest.raises(ValueError):
            Talks(title, time).create_talk()
