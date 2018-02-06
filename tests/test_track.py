from src.track import Track, NoEnoughtSpace, Scheduled
from src.talk import Talk
from datetime import datetime
import pytest


class TestSchedule:

    def test_scheduled_has_correct_title(self):
        scheduled = Scheduled("Gabizera", 60, datetime.now())

        assert scheduled.get_title() == "Gabizera"

    def test_scheduled_has_correct_duration(self):
        scheduled = Scheduled("Tutucão safado", 60, datetime.now())

        assert scheduled.duration == 60

    def test_scheduled_has_correct_date(self):
        date = datetime(2018, 1, 1, 9)
        scheduled = Scheduled("Lulinha", 60, date)

        assert scheduled.get_date() == date

    def test_scheduled_has_correct_formatted_hour_for_morning_session(self):
        date = datetime(2018, 1, 1, 9)
        scheduled = Scheduled("Lulis", 60, date)

        assert scheduled.get_hour() == '09:00AM'

    def test_scheduled_has_correct_formatted_hour_for_afternoon_session(self):
        date = datetime(2018, 1, 1, 13)
        scheduled = Scheduled("Nako", 60, date)

        assert scheduled.get_hour() == '01:00PM'

    def test_scheduled_has_correct_end_hour(self):
        date = datetime(2018, 1, 1, 13)
        end_date = datetime(2018, 1, 1, 14)
        scheduled = Scheduled("Popinha", 60, date)

        assert scheduled.get_end_hour() == end_date

    def test_scheduled_has_correct_formatted_end_hour(self):
        date = datetime(2018, 1, 1, 13)
        scheduled = Scheduled("Miauzin", 60, date)

        assert scheduled.get_formatted_end_hour() == "02:00PM"

    def test_scheduled_formatted_output(self):
        date = datetime(2018, 1, 1, 9)

        scheduled = Scheduled("Nina", 60, date)

        assert scheduled.__str__() == '09:00AM Nina 60'


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

    def test_added_a_talk_that_exceed_the_lunch_and_raises_exception(self):
        track = Track(datetime.now())
        talk = Talk("Big KeyNote", 170)
        track.schedule_talk(talk)

        talk2 = Talk("Average Talk", 30)

        with pytest.raises(NoEnoughtSpace):
            track.schedule_talk(talk2)

    def test_lunch_and_network_exists_in_track(self):
        track = Track(datetime.now())
        talk1 = Talk("Fedoka", 3 * 60)
        talk2 = Talk("Tutu de Feijão", 4 * 60)

        track.schedule_talk(talk1)
        track.schedule_talk(talk2)

        timeline_titles = [talk.title for talk in track.get_timeline()]

        assert 'Network' in timeline_titles
        assert 'Lunch' in timeline_titles

    def test_talks_is_ordered_by_hour(self):
        date = datetime(2018, 1, 1)
        track = Track(date)
        talk1 = Talk("Fedoka", 3 * 60)
        talk2 = Talk("Tutu de Feijão", 4 * 60)

        track.schedule_talk(talk1)
        track.schedule_talk(talk2)

        timeline = track.get_timeline()

        assert timeline[0].get_title() == 'Fedoka'
        assert timeline[0].get_date() == datetime(2018, 1, 1, 9)
        assert timeline[1].get_title() == 'Lunch'
        assert timeline[1].get_date() == datetime(2018, 1, 1, 12)
        assert timeline[2].get_title() == 'Tutu de Feijão'
        assert timeline[2].get_date() == datetime(2018, 1, 1, 13)
        assert timeline[3].get_title() == 'Network'
        assert timeline[3].get_date() == datetime(2018, 1, 1, 17)
