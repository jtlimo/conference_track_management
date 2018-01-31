#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import timedelta


class ScheduledTalk:

    def __init__(self, title, duration, date):
        self.date = date
        self.title = title
        self.duration = duration

    def __str__(self):
        return self.get_hour()

    def get_title(self):
        return self.title

    def get_hour(self):
        return self.date.strftime('%I:%M%p')

    def get_unformatted_hour(self):
        return self.date

    def get_end_hour(self):
        return self.get_unformatted_hour() + \
                timedelta(minutes=self.duration)

    def get_formatted_end_hour(self):
        return self.get_end_hour().strftime('%I:%M%p')

class Talk:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
