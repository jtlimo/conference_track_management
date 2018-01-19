import pytest
from track import Track
from talk import Talk
from track_management import TrackManagement
from datetime import datetime


class TestTrackManagement:

    @pytest.mark.only
    def test_with_a_full_track_returning_blocked_lunch_and_network(self):
        talk = Talk('Madokita', 3*60)
        talk2 = Talk('Tutucão', 4*60)

        tracks = TrackManagement([talk, talk2])
        tracks = tracks.generate_tracks_to_talks()

        talk_titles = [talk['title'] for talk in tracks[0]['talks']]

        assert talk.title in talk_titles
        assert talk2.title in talk_titles
        assert 'Network' in talk_titles
        assert 'Lunch' in talk_titles


    def test_when_need_to_create_a_new_track(self):
        talk = Talk('Madokita', 8*60)
        talk2 = Talk('Tutucão', 1*60)

        tracks = TrackManagement([talk, talk2])
        tracks = tracks.generate_tracks_to_talks()

        for track in tracks:
            assert track['talks'][2]['title'] is talk2.title or talk.title
            assert track['talks'][2]['duration_in_minutes'] is talk2.duration or talk.duration
            assert self.__is_empty(track) is False

    def __is_empty(self, seq):
        if not seq:
            return True
        if seq:
            return False
