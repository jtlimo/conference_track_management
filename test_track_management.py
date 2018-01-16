import pytest
from track import Track
from talk import Talk
from track_management import TrackManagement
from datetime import datetime


class TestTrackManagement:

    def test_with_a_full_track_returning_blocked_lunch_and_network(self):
        count = 0
        talk = Talk('Madokita', 3*60)
        talk2 = Talk('Tutucão', 4*60)

        tracks = TrackManagement([talk, talk2])
        tracks = tracks.generate_tracks_to_talks()

        for track in tracks:
            if talk.title is track['title']:
                count += 1
            elif talk2.title is track['title']:
                count += 1
            elif 'Lunch' is track['title']:
                count += 1
            elif 'Network' is track['title']:
                count += 1

        assert count is 4


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
