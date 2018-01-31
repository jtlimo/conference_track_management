import pytest
from track import Track
from talk import Talk
from track_management import TrackManagement
from datetime import datetime


class TestTrackManagement:
    def test_when_need_to_create_a_new_track_with_ordered_talks(self):
        talk = Talk('Madokita', 3 * 60)
        talk2 = Talk('Tutucão', 4 * 60)
        talk3 = Talk('Luna', 3 * 60)
        talk4 = Talk('Pinkudao', 4 * 60)

        tracks = TrackManagement([talk, talk2, talk3, talk4])
        tracks = tracks.generate_tracks_to_talks()

        talk_titles = self.__get_title_talks(tracks)

        assert talk.title in talk_titles[0]
        assert talk2.title in talk_titles[0]
        assert talk3.title in talk_titles[1]
        assert talk4.title in talk_titles[1]
        assert 'Network' in talk_titles[0]
        assert 'Network' in talk_titles[1]
        assert 'Lunch' in talk_titles[0]
        assert 'Lunch' in talk_titles[1]

    def test_when_need_to_create_a_new_track_with_unordered_talks(self):
        talk = Talk('Madokita', 4 * 60)
        talk2 = Talk('Tutucão', 3 * 60)
        talk3 = Talk('Luna', 3 * 60)
        talk4 = Talk('Pinkudao', 3 * 60)

        tracks = TrackManagement([talk, talk2, talk3, talk4])
        tracks = tracks.generate_tracks_to_talks()

        talk_titles = self.__get_title_talks(tracks)

        assert talk.title in talk_titles[0] or talk.title in talk_titles[1]
        assert talk2.title in talk_titles[0] or talk2.title in talk_titles[1]
        assert talk3.title in talk_titles[0] or talk3.title in talk_titles[1]
        assert talk4.title in talk_titles[0] or talk4.title in talk_titles[1]
        assert 'Network' in talk_titles[0] and 'Network' in talk_titles[1]
        assert 'Lunch' in talk_titles[0] and 'Lunch' in talk_titles[1]

    def test_safadao(self):
        talks = [
            Talk("Writing Fast Tests Against Enterprise Rails", 60),
            Talk("Overdoing it in Python", 45),
            Talk("Lua for the Masses", 30),
            Talk("Ruby Errors from Mismatched Gem Versions", 45),
            Talk("Common Ruby Errors", 45),
            Talk("Rails for Python Developers", 5),
            Talk("Communicating Over Distance", 60),
            Talk("Accounting-Driven Development", 45),
            Talk("Woah", 30),
            Talk("Sit Down and Write", 30),
            Talk("Pair Programming vs Noise", 45),
            Talk("Rails Magic", 60),
            Talk("Ruby on Rails: Why We Should Move On" , 60),
            Talk("Clojure Ate Scala (on my project)", 45),
            Talk("Programming in the Boondocks of Seattle", 30),
            Talk("Ruby vs. Clojure for Back-End Development" ,30),
            Talk("Ruby on Rails Legacy App Maintenance", 60),
            Talk("A World Without HackerNews", 30),
            Talk("User Interface CSS in Rails Apps", 30)
        ]
        track_management = TrackManagement(talks)
        tracks = track_management.generate_tracks_to_talks()

    def __get_title_talks(self, tracks):
        talk_titles = []

        for track in tracks:
            talk_titles.append([talk.get_title() for talk in
                                track.get_timeline()])

        return talk_titles
