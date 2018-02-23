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

    def test_when_delete_a_talk_by_id(self):
        self.__setup()
        self.__send_post('/talks', dict(title='Namika', duration=30))
        response = self.__send_delete('/talks/0')

        assert response.status_code == 204

    def __send_post(self, url, json_dict):
        return self.app.post(url, data=json_dict)

    def __send_delete(self, url):
        return self.app.delete(url)

    def __setup(self):
        src.web.app.testing = True
        self.app = src.web.app.test_client()
