import pytest
from track import Track
from talk import Talk
from track_management import TrackManagement
from datetime import datetime


class TestTrackManagement:

    #@pytest.mark.only
    def test_with_a_full_track_returning_blocked_lunch_and_network(self):
        talk = Talk('Madokita', 3*60)
        talk2 = Talk('Tutucão', 4*60)

        tracks = TrackManagement([talk, talk2])
        tracks = tracks.generate_tracks_to_talks()

        talk_titles = self.__get_title_talks(tracks)

        assert talk.title in talk_titles[0]
        assert talk2.title in talk_titles[0]
        assert 'Network' in talk_titles[0]
        assert 'Lunch' in talk_titles[0]

    @pytest.mark.only
    def test_when_need_to_create_a_new_track(self):
        talk = Talk('Madokita', 8*60)
        talk2 = Talk('Tutucão', 1*60)

        tracks = TrackManagement([talk, talk2])
        tracks = tracks.generate_tracks_to_talks()

        talk_titles = self.__get_title_talks(tracks)

        assert talk.title in talk_titles[0]
        assert talk2.title in talk_titles[1]
        assert 'Network' in talk_titles[0] and talk_titles[1]
        assert 'Lunch' in talk_titles[0] and talk_titles[1]

    def __get_title_talks(self, talks):
        talk_titles = []

        for talk in talks:
            talk_titles.append([titles['title'] for titles in talk[0]['talks']])

        return talk_titles
