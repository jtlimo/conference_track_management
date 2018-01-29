#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import timedelta


class ScheduledTalk:

    def __init__(self, talk, date):
        self.talk = talk
        self.date = date

    def __str__(self):
        return self.get_hour() + " " + str(self.talk)

    def get_title(self):
        return self.talk.title

    def get_hour(self):
        return self.date.strftime('%I:%M%p')

    def get_unformatted_hour(self):
        return self.date

    def get_talk(self):
        return self.talk

    def get_end_hour(self):
        return (self.get_unformatted_hour() +
                timedelta(minutes=self.get_talk().duration))

    def get_formatted_end_hour(self):
        return self.get_end_hour().strftime('%I:%M%p')

class Talk:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return self.title + " " + str(self.duration)
