import pytest
from track import Track
from talk import Talk
from track_management import TrackManagement
from datetime import datetime


class TestTrackManagement:

    @pytest.mark.first
    def test_with_a_full_track_returning_blocked_lunch_and_network(self):
        count = 0
        talk = Talk('Madokita', 3*60)
        talk2 = Talk('Tutucão', 4*60)

        manage_tracks = TrackManagement([talk, talk2])
        manage_tracks = manage_tracks.generate_tracks_to_talks()

        for track in manage_tracks:
            if talk.title is track['title']:
                count += 1
            elif talk2.title is track['title']:
                count += 1
            elif 'Lunch' is track['title']:
                count += 1
            elif 'Network' is track['title']:
                count += 1

        assert count is 4


    # def test_when_need_to_create_a_new_track(self):
    #     talk = Talk('Madokita', 5*60)
    #     talk2 = Talk('Tutucão', 1*60)
    #     talk3 = Talk('Lulis', 1*60)
    #
    #     manage_tracks = TrackManagement([talk, talk2, talk3])
    #
    #     manage_tracks = manage_tracks.generate_tracks_to_talks()
    #
    #     print(manage_tracks)
    #
    #     assert 0
