#!/usr/bin/python
# -*- coding: utf-8 -*-
from track import Track, NoEnoughtSpace
from datetime import datetime, timedelta
from uuid import uuid4


class TrackManagement:

    def __init__(self, talks):
        self.talks = talks

    def generate_tracks_to_talks(self):
        track = Track(datetime.now())
        tracks = [track]
        for talk in self.talks:
            try:
                track.schedule_talk(talk)
            except NoEnoughtSpace:
                new_track = Track(datetime.now())
                tracks.append(new_track)
                new_track.schedule_talk(track.get_scheduled_talks().pop().talk)

        self.schedule_network_for_all_tracks(tracks)
        return tracks

    def schedule_network_for_all_tracks(self, tracks):
        for track in tracks:
            track.schedule_network_event()
