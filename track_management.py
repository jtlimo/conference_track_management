#!/usr/bin/python
# -*- coding: utf-8 -*-
from track import Track, NoEnoughtSpace
from datetime import datetime, timedelta
from uuid import uuid4


class TrackManagement:

    def __init__(self, talks):
        self.talks = talks

    def generate_tracks_to_talks(self):
        track1 = Track(datetime.now())
        track2 = Track(datetime.now())
        talks = self.talks

        while talks:
            talk = talks[0]
            talks = talks[1:]
            try:
                if not track1.is_valid():
                    track1.schedule_talk(talk)
                else:
                    print('safada', talk)
                    track2.schedule_talk(talk)
            except NoEnoughtSpace:
                talks = self.get_next_talks_iteration([track1,track2], talks, talk)

        self.schedule_network_and_lunch_for_all_tracks([track1, track2])
        return track1, track2


    def schedule_network_and_lunch_for_all_tracks(self, tracks):
        for track in tracks:
            track.schedule_network_event()
            track.schedule_lunch_hour()

    def get_next_talks_iteration(self, tracks, talks, current_talk):
        track1, track2 = tracks
        added_talks = track1.get_scheduled_talks() + \
                      track2.get_scheduled_talks() + [current_talk]
        first_added = added_talks[0]
        size_talks = len(added_talks)
        head_talks = added_talks[:size_talks - 1]
        talks.append(first_added)
        return head_talks + talks
