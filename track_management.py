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
        tracks = [track]
        for talk in self.talks:
            try:
                track.schedule_talk(talk)
            except NoEnoughtSpace:
                new_track = Track(datetime.now())
                tracks.append(new_track)
                new_track.schedule_talk(track.get_scheduled_talks().pop().talk)

        return self.__formatted_track(tracks)


    #FIXME: confusing code, loop inside other loop, its weird!
    def __formatted_track(self, tracks):
        ids = []
        index = 0
        for track in tracks:
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
            index += 1

        return self.tracks
