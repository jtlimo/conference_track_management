import pytest
from Talks import Talks
from datetime import datetime, date, time, timedelta

class TestTalkValidations(object):

    def test_isminutetalk(self, time=60, track_title="track title example"):

        talk = Talks.create_talk(track_title, time)
        new_time = talk['time_of_talk'][1] - timedelta(minutes=time)

        expected_time = new_time + timedelta(minutes=time)

        assert talk['time_of_talk'][1], expected_time

    #input Writing Fast Tests Against Enterprise Rails 60min
    #output 09:00AM Writing Fast Tests Against Enterprise Rails 60min
    def test_title_talk(self, title="Writing Fast Tests Against Enterprise Rails", time=60):

        talk = Talks.create_talk(title, time)

        assert title == talk['title']

    def test_title_not_contain_numbers(self, title="Writing blabla5325", time=60):

        with pytest.raises(ValueError):
            Talks.create_talk(title, time)
