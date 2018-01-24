#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import timedelta
from talk import Talk

class ScheduledTalk:
    def __init__(self, talk, date):
        self.talk = talk
        self.date = date

    def __str__(self):
        return self.get_hour() + " " + self.talk

    def get_title(self):
        return self.talk.title

    def get_hour(self):
        return self.date.strftime('%I:%M%p')


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
        self.__schedule_lunch_hour()
        self.__schedule_network_event()

    def is_valid(self):
        self.filtered_hours = []
        for talk in self.get_scheduled_talks():
            self.filtered_hours.append(talk.date <= self.deadline_talk)

        return all(self.filtered_hours)

    def schedule_talk(self, talk):
        scheduled = ScheduledTalk(talk, self.next_date)
        self.scheduled_talks.append(scheduled)
        self.next_date = self.next_date + timedelta(minutes=talk.duration)
        self.__can_schedule(scheduled)

    def __schedule_lunch_hour(self):
        scheduled = ScheduledTalk(Talk('Lunch', 60), self.lunch_hour)
        self.scheduled_talks.append(scheduled)

    def __schedule_network_event(self):
        scheduled = ScheduledTalk(Talk('Network', 60), self.deadline_talk)
        self.scheduled_talks.append(scheduled)

    def get_scheduled_talks(self):
        return self.scheduled_talks

    def __can_schedule(self, talk):
        if talk.date >= self.deadline_talk:
            raise NoEnoughtSpace
        elif self.__is_lunch_hour():
            self.__reeschedule_talk_after_lunch()

    def __is_lunch_hour(self):
        return (self.next_date >= self.lunch_hour and
                self.next_date <= self.end_lunch)

    def __reeschedule_talk_after_lunch(self):
        self.next_date = self.next_date.replace(
            hour=self.end_lunch.hour,
            minute=self.end_lunch.minute,
            second=self.end_lunch.second,
            microsecond=self.end_lunch.microsecond)
