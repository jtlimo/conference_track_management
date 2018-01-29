#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import timedelta, datetime
from talk import Talk, ScheduledTalk
from copy import copy


class NoEnoughtSpace(Exception):
    pass


class Track:
    def __init__(self, date):
        self.next_date = self.__reset_hour()
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
        # import pdb; pdb.set_trace()
        scheduled = ScheduledTalk(talk, self.next_date)
        self.scheduled_talks.append(scheduled)
        self.next_date = self.next_date + timedelta(minutes=talk.duration)
        if self.__is_lunch_hour(scheduled):
            self.__reeschedule_talk_after_lunch()
        elif self.__cant_schedule(scheduled):
            self.__reset_hour()
            self.scheduled_talks = self.__remove_last_talk()[1]
            raise NoEnoughtSpace

    def __reset_hour(self, date=datetime.now()):
        self.next_date = date.replace(hour=9, minute=0, second=0,
                                      microsecond=0)
        return self.next_date

    def __remove_last_talk(self):
        # import pdb; pdb.set_trace()
        next_scheduled = self.scheduled_talks.pop()
        scheduled_talks_shadow = self.scheduled_talks.copy()
        self.scheduled_talks.clear()
        return next_scheduled, scheduled_talks_shadow

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

    def __cant_schedule(self, talk):
        return (talk.get_unformatted_hour() >= self.deadline_talk and
                talk.get_end_hour() >= self.deadline_talk)

    def __is_lunch_hour(self, talk):
        # import pdb; pdb.set_trace()
        return (self.next_date >= self.lunch_hour and
                self.next_date <= self.end_lunch or
                talk.get_end_hour() > self.lunch_hour and
                talk.get_end_hour() <= self.end_lunch)

    def __reeschedule_talk_after_lunch(self):
        self.next_date = self.next_date.replace(
            hour=self.end_lunch.hour,
            minute=self.end_lunch.minute,
            second=self.end_lunch.second,
            microsecond=self.end_lunch.microsecond)
