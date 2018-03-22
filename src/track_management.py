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
        talks_combinations = self.__get_talks_combinations(self.talks)
        self.tracks.append(Track(datetime.now()))
        
        print("combinations",talks_combinations)
        for talks in talks_combinations:
            print(talks)
            if not talks:
               return self.tracks_full + self.talks    
            for talk in talks:
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
                    #talks = self.__get_changed_talks()

        return self.tracks_full + self.tracks

    def __restart_tracks(self):
        self.tracks.clear()
        self.tracks_full.clear()
        self.tracks.append(Track(datetime.now()))

    def __get_changed_talks(self):
        random.shuffle(self.talks)
        talks = self.talks
        return talks
        
    def __get_talks_combinations(self, talks, talks_original_order = [], talks_combinations=[]):
        print([talk.title for talk in talks]) 
        if not talks_original_order:
            talks_original_order = talks.copy()
        for index, talk in enumerate(talks):
            i = index + 1
            if i > len(talks) - 1:
                if talks == talks_original_order:
                    return talks_combinations
                self.__get_talks_combinations(talks, talks_original_order)
            else:
                talks_combinations.append(talks.copy())
                talks[index] = talks[index + 1]
                talks[index + 1] = talk
                print([talk.title for talk in talks]) 
