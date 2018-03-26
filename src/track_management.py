#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.track import Track, NoEnoughtSpace
from datetime import datetime


class TrackManagement:

    def __init__(self, talks):
        self.talks = talks
        self.tracks = []
        self.tracks_full = []
        self.talks_combinations = []

    def generate_tracks_to_talks(self):
        talks_combinations = self.__get_talks_combinations(self.talks)
        self.tracks.append(Track(datetime.now()))
        for combinations in talks_combinations:
            for talk in combinations:
                try:
                    self.__insert_talk_in_track(talk)
                except NoEnoughtSpace:
                    self.__restart_tracks()
            if self.__all_generated_tracks_are_fully():
                 return self.tracks_full + self.tracks
        return self.tracks_full + self.tracks
    
    def __all_generated_tracks_are_fully(self):
        for track_full, tracks in zip(self.tracks_full, self.tracks):
            return track_full.is_full() and tracks.is_full()
                
    def __insert_talk_in_track(self, talk):
        for track in self.tracks:
            if not track.is_full():
                track.schedule_talk(talk)
            else:
                self.__create_a_new_track_after_stock_a_fully_track(track)

    def __restart_tracks(self):
        self.tracks.clear()
        self.tracks_full.clear()
        self.tracks.append(Track(datetime.now()))

    def __create_a_new_track_after_stock_a_fully_track(self, current_track):
        self.tracks_full.append(current_track)
        self.tracks.append(Track(datetime.now()))
        self.tracks = self.tracks[1:]

    def __get_talks_combinations(self, talks, talks_original_order = [], talks_combinations=[]):
        if not talks_original_order:
            talks_original_order = talks.copy()
        for index, talk in enumerate(talks):
            i = index + 1
            if i > len(talks) - 1:
                if talks == talks_original_order:
                    break
                self.__get_talks_combinations(talks, talks_original_order)
            else:
                self.talks_combinations.append(talks.copy())
                talks[index] = talks[index + 1]
                talks[index + 1] = talk
        return self.talks_combinations
