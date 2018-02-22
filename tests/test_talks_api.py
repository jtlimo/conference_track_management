import pytest
import src.web
from src.talk import Talk
from flask import json


class TestTalksAPI:

    def test_when_insert_a_talk(self):
        self.__setup()
        response = self.__send_post('/talks', dict(title='Namika',
                                                   duration=30))
        data = json.loads(response.data)

        assert data['id'] == 0
        assert data['title'] == 'Namika'
        assert data['duration'] == 30

    def __send_post(self, url, json_dict):
        return self.app.post(url, data=json_dict)

    def __setup(self):
        src.web.app.testing = True
        self.app = src.web.app.test_client()
