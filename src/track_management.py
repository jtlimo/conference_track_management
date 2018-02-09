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

    def generate_tracks_to_talks(self):
        talks = self.talks
        self.tracks.append(Track(datetime.now()))
        tracks_full = []
        for _ in repeat(talks, factorial(len(talks))):
            if not talks: return tracks_full + self.tracks
            talk = talks[0]
            talks = talks[1:]
            try:
                for track in self.tracks:
                    if not track.is_full():
                        track.schedule_talk(talk)
                    else:
                        tracks_full.append(track)
                        self.tracks.append(Track(datetime.now()))
                        self.tracks = self.tracks[1:]
            except NoEnoughtSpace:
                self.__restart_tracks(tracks_full)

        return tracks_full + self.tracks


    def __restart_tracks(self, tracks_full):
        self.tracks.clear()
        tracks_full.clear()
        self.tracks.append(Track(datetime.now()))
        random.shuffle(self.talks)
        talks = self.talks
