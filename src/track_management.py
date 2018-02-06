#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.track import Track, NoEnoughtSpace
from datetime import datetime
import random

class TrackManagement:

    def __init__(self, talks):
        self.talks = talks
        self.tracks = []

    def generate_tracks_to_talks(self):
        talks = self.talks
        self.tracks.append(Track(datetime.now()))
        print('criei a track joça véia')
        while talks:
            talk = talks[0]
            talks = talks[1:]
            try:
                for track in self.tracks:
                    if not track.is_valid():
                        print('trying to schedule the talk:', talk.title)
                        track.schedule_talk(talk)
                    else:
                        print('creating a new track cause the track is completed')
                        self.tracks.append(Track(datetime.now()))
            except NoEnoughtSpace:
                print('initializing all tracks again, no enought space for this talk:', talk.title)
                self.tracks.clear()
                self.tracks.append(Track(datetime.now()))
                random.shuffle(self.talks)
                talks = self.talks

        for tracks in self.tracks:
            for index, track in enumerate(tracks.get_timeline()):
                print(index, track)

        return self.tracks
