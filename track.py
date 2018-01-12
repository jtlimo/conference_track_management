#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import timedelta


class ScheduledTalk:
    def __init__(self, talk, date):
        self.talk = talk
        self.date = date


class NoEnoughtSpace(Exception):
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
        self.end_lunch = date.replace(hour=13, minute=0, second=0,
                                      microsecond=0)

    def is_valid(self):
        self.filtered_hours = []

        for talk in self.get_scheduled_talks():
            self.filtered_hours.append(talk.date <= self.deadline_talk)

        return all(self.filtered_hours)

    def schedule_talk(self, talk):
        scheduled = ScheduledTalk(talk, self.next_date)
        self.scheduled_talks.append(scheduled)
        self.next_date = self.next_date + timedelta(minutes=talk.duration)
        self.can_schedule(scheduled)

    def get_scheduled_talks(self):
        return self.scheduled_talks

    def can_schedule(self, talk):
        if talk.date >= self.deadline_talk:
            raise NoEnoughtSpace
        elif self.is_lunch_hour():
            self.reeschedule_talk_after_lunch()

    def is_lunch_hour(self):
        return (self.next_date >= self.lunch_hour and
                self.next_date <= self.end_lunch)

    def reeschedule_talk_after_lunch(self):
        self.next_date = self.next_date.replace(
            hour=self.end_lunch.hour,
            minute=self.end_lunch.minute,
            second=self.end_lunch.second,
            microsecond=self.end_lunch.microsecond)
