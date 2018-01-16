#!/usr/bin/python
# -*- coding: utf-8 -*-
from track import Track, NoEnoughtSpace
from datetime import datetime, timedelta
from uuid import uuid4


class TrackManagement:

    def __init__(self, talks):
        self.tracks = []
        self.talks = talks

    def generate_tracks_to_talks(self):
        track = Track(datetime.now())
        for talk in self.talks:
            try:
                track.schedule_talk(talk)
            except NoEnoughtSpace:
                new_track = Track(datetime.now())
                new_track.schedule_talk(track.get_scheduled_talks().pop().talk)

        #FIXME: I broked this! Fuck!!! UnboundLocalError: local variable
        # 'new_track' referenced before assignment
        if track.is_valid() and new_track.is_valid():
            return self.__formatted_track(track, new_track)


    #FIXME: confusing code, loop inside other loop, its weird!
    def __formatted_track(self, *tracks):
        ids = []
        for index, track in enumerate(tracks):
            ids = str(uuid4())
            self.tracks.append({'id': ids, 'talks': []})
            for scheduled in track.get_scheduled_talks():
                end_talk = scheduled.date + timedelta(minutes=scheduled.talk.duration)
                self.tracks[index]['talks'].append({'hour': scheduled.date.strftime('%I:%M%p'),
                                     'title': scheduled.talk.title,
                                     'duration_in_minutes':
                                     scheduled.talk.duration,
                                     'end_of_talk':
                                     end_talk.strftime('%I:%M%p')})
        return self.tracks
