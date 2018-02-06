from src.track import Track
from src.talk import Talk
from src.track_management import TrackManagement
from src.conference import Conference
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
        track_management = TrackManagement(talks)
        tracks = track_management.generate_tracks_to_talks()
        conference = Conference(tracks)

        conference = conference.get_formatted_tracks_for_conference()

        assert conference == {'Track 1': ['09:00AM Xuxu 180',
                                          '12:00PM Lunch 60',
                                          '01:00PM Abacaxi 240',
                                          '05:00PM Network 60'],
                              'Track 2':
                                         ['09:00AM Couve 180',
                                          '12:00PM Lunch 60',
                                          '01:00PM Frango 240',
                                          '05:00PM Network 60']}
