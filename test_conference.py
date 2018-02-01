import pytest
from track import Track
from talk import Talk
from track_management import TrackManagement
from conference import Conference
from datetime import datetime


class TestConference:

    def test_when_return_the_conference_complete(self):
        track = Track(datetime.now())
        talks = [
                 Talk("Xuxu", 3 * 60),
                 Talk("Abacaxi", 4 * 60),
                 Talk("Couve", 3 * 60),
                 Talk("Frango", 4 * 60)
                ]
        tracks = TrackManagement(talks)
        conference = Conference(tracks)

        conference = conference.get_formatted_tracks_for_conference()

        assert conference is "Track 1:\n\
                              09:00AM Xuxu 180\
                              12:00PM Lunch 60\
                              13:00PM Abacaxi 240\
                              17:00PM Network 60\n\
                              Track 2:\n\
                              09:00AM Couve 180\
                              12:00PM Lunch 60\
                              13:00PM Frango 240\
                              17:00PM Network 60"
