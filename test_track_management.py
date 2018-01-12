import pytest
from track import Track
from talk import Talk
from track_management import TrackManagement
from datetime import datetime


class TestTrackManagement:

    @pytest.mark.first
    def test_when_need_to_create_a_new_track(self):
        talk = Talk('Madokita', 7*60)
        talk2 = Talk('Tutucão', 1*60)
        talk3 = Talk('Lulis', 1*60)

        manage_tracks = TrackManagement([talk, talk2, talk3])

        manage_tracks = manage_tracks.generate_tracks_to_talks()

        print(manage_tracks)

        assert 0
