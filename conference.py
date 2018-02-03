#!/usr/bin/python
# -*- coding: utf-8 -*-


class Conference:

    def __init__(self, tracks):
        self.tracks = tracks

    def get_formatted_tracks_for_conference(self):
        formatted_conference = {}
        for i, track in enumerate(self.tracks):
            formatted_conference["Track" + " " +
                                 str(i + 1)] = [str(timeline)
                                                for timeline in
                                                track.get_timeline()]
        return formatted_conference
