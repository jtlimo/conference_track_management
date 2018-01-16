import pytest
from track import Track, NoEnoughtSpace
from talk import Talk
from datetime import datetime


class TestTrackSchedule:

    def test_when_a_talk_is_added_in_an_empty_track(self):
        track = Track(datetime.now())
        talk = Talk("qualquer bosta", 60)
        track.schedule_talk(talk)

        # I had previous talks: lunch and network event
        assert len(track.scheduled_talks) == 3


    def test_talk_is_added_correctly(self):
        track = Track(datetime.now())
        talk = Talk("qualquer bosta denovo", 60)
        track.schedule_talk(talk)

        scheduled = track.scheduled_talks[2]

        assert scheduled.talk == talk
        assert scheduled.date.hour == 9
        assert scheduled.date.minute == 0
        assert scheduled.date.second == 0
        assert scheduled.date.microsecond == 0

    def test_that_the_talk_date_is_based_on_previous_talk(self):
        track = Track(datetime.now())
        talk = Talk("qualquer bosta denovo", 30)
        track.schedule_talk(talk)

        talk2 = Talk("bostona veia", 30)
        track.schedule_talk(talk2)
        scheduled = track.scheduled_talks[3]

        assert scheduled.talk == talk2
        assert scheduled.date.hour == 9
        assert scheduled.date.minute == 30
        assert scheduled.date.second == 0
        assert scheduled.date.microsecond == 0

    def test_that_i_cant_add_a_talk_when_track_is_full(self):
        track = Track(datetime.now())
        talk = Talk("Really Large Talk", 8 * 60)
        track.schedule_talk(talk)

        talk2 = Talk("bostona veia", 30)

        with pytest.raises(NoEnoughtSpace):
            track.schedule_talk(talk2)

    def test_that_i_reeschedule_a_talk_when_is_the_lunch_hour(self):
        track = Track(datetime.now())
        talk = Talk("Talk 1", 3 * 60)
        track.schedule_talk(talk)

        talk2 = Talk("Talk on the lunch hour", 30)

        track.schedule_talk(talk2)
        scheduled = track.scheduled_talks[3]

        assert scheduled.talk == talk2
        assert scheduled.date.hour == 13
        assert scheduled.date.minute == 0
        assert scheduled.date.second == 0
        assert scheduled.date.microsecond == 0

    def test_track_is_completed_correctly(self):
        track = Track(datetime.now())
        talk = Talk("first talk", 3 * 60)
        track.schedule_talk(talk)

        talk2 = Talk("Talk 2", 4 * 60)
        track.schedule_talk(talk2)

        assert track.is_valid() is True
