import pytest
from track import Track, NoEnoughtSpace
from talk import Talk
from datetime import datetime


class TestTrackSchedule:

    def test_when_a_talk_is_added_in_an_empty_track(self):
        track = Track(datetime.now())
        talk = Talk("qualquer bosta", 60)
        track.schedule_talk(talk)

        assert len(track.get_timeline()) == 3

    def test_talk_is_added_correctly(self):
        track = Track(datetime.now())
        talk = Talk("qualquer bosta denovo", 60)
        track.schedule_talk(talk)

        scheduled = track.get_timeline()[0]

        assert scheduled.title == talk.title
        assert scheduled.duration == talk.duration
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
        scheduled = track.get_timeline()[1]

        assert scheduled.title == talk2.title
        assert scheduled.duration == talk2.duration
        assert scheduled.date.hour == 9
        assert scheduled.date.minute == 30
        assert scheduled.date.second == 0
        assert scheduled.date.microsecond == 0

    def test_that_i_cant_add_a_talk_when_track_is_full(self):
        track = Track(datetime.now())
        talk = Talk("Really Large Talk", 3 * 60)
        track.schedule_talk(talk)
        talk2 = Talk("Really Large Talk", 4 * 60)
        track.schedule_talk(talk2)

        talk3 = Talk("bostona veia", 30)

        with pytest.raises(NoEnoughtSpace):
            track.schedule_talk(talk3)

    def test_that_i_reeschedule_a_talk_when_is_the_lunch_hour(self):
        track = Track(datetime.now())
        talk = Talk("Talk 1", 3 * 60)
        track.schedule_talk(talk)

        talk2 = Talk("Talk on the lunch hour", 30)

        track.schedule_talk(talk2)
        scheduled = track.get_timeline()[2]

        assert scheduled.title == talk2.title
        assert scheduled.duration == talk2.duration
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

    def test_track_is_completed_correctly_when_network_starts_at_16h(self):
        track = Track(datetime.now())
        talk = Talk("first talk", 3 * 60)
        track.schedule_talk(talk)

        talk2 = Talk("Talk 2", 3 * 60)
        track.schedule_talk(talk2)

        assert track.is_valid() is True

    def test_track_is_not_valid(self):
        track = Track(datetime.now())
        talk = Talk("first talk", 3 * 60)
        track.schedule_talk(talk)

        talk2 = Talk("Talk 2", 2 * 60)
        track.schedule_talk(talk2)

        assert track.is_valid() is False

    def test_when_added_a_talk_that_exceed_the_lunch_time_it_raises_an_exception(self):
        track = Track(datetime.now())
        talk = Talk("Big KeyNote", 170)
        track.schedule_talk(talk)

        talk2 = Talk("Average Talk", 30)

        with pytest.raises(NoEnoughtSpace):
            track.schedule_talk(talk2)
