import unittest
from Talks import Talks
from datetime import datetime, date, time, timedelta

class TestTrackTime(unittest.TestCase):
    
    def test_isminutetrack(self, time=60, track_title="track title example"):
        talk = Talks(track_title, time)
        talk_time = talk.get_a_time_to_talk(talk.duration)

        new_time = talk[1] - timedelta(minutes=talk.duration)

        expected_time = new_time + timedelta(minutes=talk.duration)
        self.assertEqual(talk, expected_time)


if __name__ == '__main__':
    unittest.main()
