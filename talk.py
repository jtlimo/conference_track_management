#!/usr/bin/python
# -*- coding: utf-8 -*-


class Talk:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        #Writing Fast Tests Against Enterprise Rails 60min
        return self.title + " " + self.duration
