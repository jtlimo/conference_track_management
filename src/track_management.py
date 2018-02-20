#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import repeat
from src.track import Track, NoEnoughtSpace
from datetime import datetime
from math import factorial
import random


class TrackManagement:

    def __init__(self, talks):
        self.talks = talks
        self.tracks = []
        self.tracks_full = []

    def generate_tracks_to_talks(self):
        talks = self.talks
        self.tracks.append(Track(datetime.now()))
        for _ in repeat(talks, factorial(len(talks))):
            if not talks:
                return self.tracks_full + self.tracks
            talk = talks[0]
            talks = talks[1:]
            try:
                for track in self.tracks:
                    if not track.is_full():
                        track.schedule_talk(talk)
                    else:
                        self.tracks_full.append(track)
                        self.tracks.append(Track(datetime.now()))
                        self.tracks = self.tracks[1:]
            except NoEnoughtSpace:
                self.__restart_tracks()
                talks = self.__get_changed_talks()

        return self.tracks_full + self.tracks

    def __restart_tracks(self):
        self.tracks.clear()
        self.tracks_full.clear()
        self.tracks.append(Track(datetime.now()))

    def __get_changed_talks(self):
        random.shuffle(self.talks)
        talks = self.talks
        return talks
