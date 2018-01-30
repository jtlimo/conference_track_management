import pytest
from track import Track
from talk import Talk
from track_management import TrackManagement
from datetime import datetime


class TestTrackManagement:

    def test_with_a_full_track_returning_blocked_lunch_and_network(self):
        talk = Talk('Madokita', 3 * 60)
        talk2 = Talk('Tutucão', 4 * 60)

        tracks = TrackManagement([talk, talk2])
        tracks = tracks.generate_tracks_to_talks()

        talk_titles = self.__get_title_talks(tracks)

        assert talk.title in talk_titles[0]
        assert talk2.title in talk_titles[0]
        assert 'Network' in talk_titles[0]
        assert 'Lunch' in talk_titles[0]

    def test_when_need_to_create_a_new_track(self):
        talk = Talk('Madokita', 8 * 60)
        talk2 = Talk('Tutucão', 1 * 60)

        tracks = TrackManagement([talk, talk2])
        tracks = tracks.generate_tracks_to_talks()

        talk_titles = self.__get_title_talks(tracks)

        assert talk.title in talk_titles[0]
        assert talk2.title in talk_titles[1]
        assert 'Network' in talk_titles[0] and talk_titles[1]
        assert 'Lunch' in talk_titles[0] and talk_titles[1]

    def test_when_schedule_network_event_after_a_small_talk(self):
        talk = Talk('Madokita', 3 * 60)
        talk2 = Talk('Tutucão', 1 * 60)

        tracks = TrackManagement([talk, talk2])
        tracks = tracks.generate_tracks_to_talks()

        talk_hours = self.__get_hour_talks(tracks)
        talk_titles = self.__get_title_talks(tracks)

        for title, hour in zip(talk_titles, talk_hours):
            assert talk.title in title
            assert talk2.title in title
            assert 'Network' in title
            assert '04:00PM' == hour[-1]

    @pytest.mark.only
    def test_when_need_to_create_more_than_two_tracks(self):
        talk = Talk('Madokita', 3 * 60)
        talk2 = Talk('Tutucão', 2 * 60)
        talk3 = Talk('Luna', 2 * 60)
        talk4 = Talk('Pink', 3 * 60)
        talk5 = Talk('Nick', 2 * 60)
        talk6 = Talk('Greg', 2 * 60)
        talk7 = Talk('Paola', 3 * 60)
        talk8 = Talk('Miauzin', 2 * 60)
        talk9 = Talk('Popinha', 2 * 60)

        tracks = TrackManagement([talk, talk2, talk3, talk4, talk5, talk6,
                                  talk7, talk8, talk9])
        tracks.generate_tracks_to_talks()

        assert 0

    def __get_title_talks(self, tracks):
        talk_titles = []

        for track in tracks:
            talk_titles.append([talk.get_title() for talk in
                                track.get_scheduled_talks()])

        return talk_titles

    def __get_hour_talks(self, tracks):
        talk_hours = []

        for track in tracks:
            talk_hours.append([talk.get_hour() for talk in
                               track.get_scheduled_talks()])

        return talk_hours
