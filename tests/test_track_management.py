from src.track import Track
from src.talk import Talk
from src.track_management import TrackManagement
from datetime import datetime
import pytest


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

    @pytest.mark.only
    def test_when_need_to_create_a_new_track_with_unordered_talks(self):
        talk = Talk('Madokita', 4 * 60)
        talk2 = Talk('Tutucão', 3 * 60)
        talk3 = Talk('Luna', 3 * 60)
        talk4 = Talk('Pinkudao', 3 * 60)

        tracks = TrackManagement([talk, talk2, talk3, talk4])
        tracks = tracks.generate_tracks_to_talks()

        talk_titles = self.__get_title_talks(tracks)

        assert 0
        assert talk.title in talk_titles[0] or talk.title in talk_titles[1]
        assert talk2.title in talk_titles[0] or talk2.title in talk_titles[1]
        assert talk3.title in talk_titles[0] or talk3.title in talk_titles[1]
        assert talk4.title in talk_titles[0] or talk4.title in talk_titles[1]
        assert 'Network' in talk_titles[0] and 'Network' in talk_titles[1]
        assert 'Lunch' in talk_titles[0] and 'Lunch' in talk_titles[1]

    def __get_title_talks(self, tracks):
        talk_titles = []

        for track in tracks:
            talk_titles.append([talk.get_title() for talk in
                                track.get_timeline()])

        return talk_titles
