#!/usr/bin/python
# -*- coding: utf-8 -*-
from track import Track, NoEnoughtSpace
from datetime import datetime, timedelta
import random


class TrackManagement:

    def __init__(self, talks):
        self.talks = talks

    def generate_tracks_to_talks(self):
        track1 = Track(datetime.now())
        track2 = Track(datetime.now())
        talks = self.talks

        while talks:
            talk = talks[0]
            talks = talks[1:]
            try:
                if not track1.is_valid():
                    track1.schedule_talk(talk)
                else:
                    track2.schedule_talk(talk)
            except NoEnoughtSpace:
                track1 = Track(datetime.now())
                track2 = Track(datetime.now())
                random.shuffle(self.talks)
                talks = self.talks

        return track1, track2
