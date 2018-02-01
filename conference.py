#!/usr/bin/python
# -*- coding: utf-8 -*-

class Conference:

    def __init__(self, tracks):
        self.tracks = tracks

    def get_formatted_tracks_for_conference(self):
        formatted_conference = ""
        for i, track in enumerate(self.tracks):
            for timeline in track.get_timeline():
                 formatted_conference = "Track " + str(i + 1) + ":\n " + \
                 str(timeline)
        return formatted_conference
