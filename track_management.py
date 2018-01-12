#!/usr/bin/python
# -*- coding: utf-8 -*-
from track import Track, NoEnoughtSpace
from datetime import datetime, timedelta


class TrackManagement:

    def __init__(self, talks):
        self.talks = talks
        self.tracks = []

    def generate_tracks_to_talks(self):
        self.tracks.append(Track(datetime.now()))
        for talk, track in zip(self.talks, self.tracks):
            try:
                print('try----------', talk.title)
                print('try----------', track.next_date)

                track.schedule_talk(talk)
            except NoEnoughtSpace:
                # pass
                print('except----------', talk.title)
                # Track(datetime.now()).schedule_talk(talk)
                # #track.schedule_talk(talk)
                # print('except----------2', talk.title)

        if track.is_valid():
            return self.__formatted_track(Track(datetime.now()))
            # for track in self.tracks:
            #     print(track.get_scheduled_talks().date)

    def __formatted_track(self, track):
        formatted_tracks = []
        for output in track.get_scheduled_talks():
            formatted_tracks.append({'hour': output.date.strftime('%I:%M%p'),
                                     'title': output.talk.title,
                                     'duration_in_minutes':
                                     output.talk.duration,
                                     'end_of_talk_hour': output.date +
                                     timedelta(minutes=output.talk.duration)})

        return formatted_tracks
