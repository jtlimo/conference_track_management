#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import timedelta


class ScheduledTalk:
    def __init__(self, talk, date):
        self.talk = talk
        self.date = date


class NoEnoughtSpace(Exception):
    pass


class UnavailableHourForTalk(Exception):
    pass


class Track:
    def __init__(self, date):
        self.next_date = date.replace(hour=9, minute=0, second=0,
                                      microsecond=0)
        self.scheduled_talks = []
        self.deadline_talk = date.replace(hour=17, minute=0, second=0,
                                          microsecond=0)
        self.lunch_hour = date.replace(hour=12, minute=0, second=0,
                                       microsecond=0)
        self.end_lunch_hour = date.replace(hour=13, minute=0, second=0,
                                           microsecond=0)

    def schedule_talk(self, talk):
        scheduled = ScheduledTalk(talk, self.next_date)
        self.scheduled_talks.append(scheduled)
        self.next_date = self.next_date + timedelta(minutes=talk.duration)
        self.check_if_is_valid_hour()

    def check_if_is_valid_hour(self):
        if self.next_date > self.deadline_talk:
            raise NoEnoughtSpace
        elif (self.next_date > self.lunch_hour and
              self.next_date <= self.end_lunch_hour):
            raise UnavailableHourForTalk
