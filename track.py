#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import timedelta, datetime
from talk import Talk, ScheduledTalk
from copy import copy


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
        self.first_hour_network = date.replace(hour=16, minute=0, second=0,
                                               microsecond=0)
        self.__schedule_lunch_hour()

    def is_valid(self):
        self.filtered_hours = []
        for talk in self.get_scheduled_talks():
            self.filtered_hours.append(talk.date <= self.deadline_talk)

        return all(self.filtered_hours)

    def schedule_talk(self, talk):
        if not self.__can_schedule(talk):
            raise NoEnoughtSpace
        scheduled = ScheduledTalk(talk, self.next_date)
        self.scheduled_talks.append(scheduled)
        if scheduled.get_end_hour() == self.lunch_hour:
            self.__reeschedule_talk_after_lunch()
        else:
            self.next_date = scheduled.get_end_hour()

    def __schedule_lunch_hour(self):
        scheduled = ScheduledTalk(Talk('Lunch', 60), self.lunch_hour)
        self.scheduled_talks.append(scheduled)

    def schedule_network_event(self):
        self.__is_a_valid_hour_for_network_event()
        self.next_date = (self.next_date +
                          timedelta(minutes=self.next_date.minute))
        scheduled = ScheduledTalk(Talk('Network', 60), self.next_date)
        self.scheduled_talks.append(scheduled)

    def __is_a_valid_hour_for_network_event(self):
        if self.next_date <= self.first_hour_network:
            self.next_date = self.first_hour_network
        elif self.next_date >= self.deadline_talk:
            self.next_date = self.deadline_talk

    def get_scheduled_talks(self):
        return self.scheduled_talks

    def __can_schedule(self, talk):
        talk_end = self.next_date + timedelta(minutes=talk.duration)
        if talk_end > self.lunch_hour and self.next_date < self.lunch_hour:
            return False
        if talk_end > self.deadline_talk:
            return False
        return True

    def __reeschedule_talk_after_lunch(self):
        self.next_date = self.next_date.replace(
            hour=self.end_lunch.hour,
            minute=self.end_lunch.minute,
            second=self.end_lunch.second,
            microsecond=self.end_lunch.microsecond)
