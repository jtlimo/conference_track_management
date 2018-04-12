import pytest
import src.web
from unittest.mock import patch
from src.talk import Talk
from flask import json
from src.web.talks_repository import TalkNotFoundException

class TestTalksAPI:

    @patch('src.web.TalksRepository.insert', return_value= 0)
    @patch('src.web.TalksRepository.get', return_value=Talk('Namika', 30))
    def test_when_insert_a_talk(self, mock_repo_get, mock_repo_insert):
        response = self.__send_post('/talks', dict(title='Namika', duration=30))

        mock_repo_get.return_value = [Talk('Namika', 30)]
        data = json.loads(response.data)

        assert data['id'] == 0
        assert data['title'] == 'Namika'
        assert data['duration'] == 30
       
        assert len(mock_repo_get()) == 1

    @patch('src.web.TalksRepository.delete', return_value=[])
    def test_when_delete_a_talk_by_id(self, mock_delete):
        response = self.__send_delete('/talks/0')
        
        assert response.status_code == 204
        assert len(mock_delete()) == 0

    @patch('src.web.TalksRepository.delete', side_effect=TalkNotFoundException)
    def test_when_delete_an_inexistent_talk(self, mock_delete):
        response = self.__send_delete('/talks/0')
        with pytest.raises(TalkNotFoundException):
            mock_delete()
        
        assert response.status_code == 404
    
    def test_when_insert_multiple_talks_then_return_a_list_of_talks(self):
        self.__send_post('/talks', dict(title='Namika', duration=30))
        self.__send_post('/talks', dict(title='Luna',duration=30))
        self.__send_post('/talks', dict(title='Pink',duration=30))
        response = self.__send_get('/talks') 
        data = json.loads(response.data)

        assert data[0]['id'] == 0
        assert data[0]['title'] == 'Namika'
        assert data[0]['duration'] == 30
        assert data[1]['id'] == 1
        assert data[1]['title'] == 'Luna'
        assert data[1]['duration'] == 30
        assert data[2]['id'] == 2
        assert data[2]['title'] == 'Pink'
        assert data[2]['duration'] == 30

    @pytest.fixture(autouse=True)
    def test_configuration(self):
        self.__setup()
        yield
        self.__teardown()

    def __send_post(self, url, json_dict):
        return self.app.post(url, data=json_dict)

    def __send_delete(self, url):
        return self.app.delete(url)

    def __send_get(self,url):
        return self.app.get(url)

    def __setup(self):
        src.web.app.testing = True
        self.app = src.web.app.test_client()

    def __teardown(self):
        self.__clear_repository()

    def __clear_repository(self):
         response = self.__send_get('/talks')
         talks = json.loads(response.data)
         for index, talk in enumerate(talks):
             self.__send_delete('/talks/{}'.format(index))
