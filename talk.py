#!/usr/bin/python
# -*- coding: utf-8 -*-


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

    def get_talk(self):
        return self.talk


class Talk:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return self.title + " " + str(self.duration)
