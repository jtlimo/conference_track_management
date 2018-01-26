#!/usr/bin/python
# -*- coding: utf-8 -*-
from track import Track, NoEnoughtSpace
from datetime import datetime, timedelta
from uuid import uuid4


class TrackManagement:

    def __init__(self, talks):
        self.talks = talks

    # TODO: Generate 1...n tracks
    def generate_tracks_to_talks(self):
        track = Track(datetime.now())
        tracks = [track]
        for talk in self.talks:
            try:
                track.schedule_talk(talk)
            except NoEnoughtSpace:
                new_track = Track(datetime.now())
                tracks.append(new_track)
                # FIXME: Move changes to list of talks to Talk class
                new_track.schedule_talk(talk)

        self.schedule_network_for_all_tracks(tracks)
        return tracks

    def schedule_network_for_all_tracks(self, tracks):
        for track in tracks:
            track.schedule_network_event()
