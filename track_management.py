#!/usr/bin/python
# -*- coding: utf-8 -*-
from track import Track, NoEnoughtSpace
from datetime import datetime, timedelta
from uuid import uuid4


class TrackManagement:

    def __init__(self, talks):
        #self.tracks = [{'id': str(uuid4()), 'track':  '', 'talks': []}]
        self.talks = talks

    def generate_tracks_to_talks(self):
        track = Track(datetime.now())
        for talk in self.talks:
            try:
                track.schedule_talk(talk)
            except NoEnoughtSpace:
                pass

        if track.is_valid():
            return self.__formatted_track(track)

    def __formatted_track(self, track):
        formatted_tracks = []
        for output in track.get_scheduled_talks():
            end_talk = output.date + timedelta(minutes=output.talk.duration)
            formatted_tracks.append({'hour': output.date.strftime('%I:%M%p'),
                                     'title': output.talk.title,
                                     'duration_in_minutes':
                                     output.talk.duration,
                                     'end_of_talk':
                                     end_talk.strftime('%I:%M%p')})
        return formatted_tracks
