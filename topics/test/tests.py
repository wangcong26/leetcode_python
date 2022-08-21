import unittest
import responses
from main import get_joke
import requests

class TestGetJoke(unittest.TestCase):

    @responses.activate
    def test_get_joke_returns_a_joke(self):
        responses.get(
            url='http://api.icndb.com/jokes/random',
            json = {'value':{'joke':'hello world'}},
            status=200
        )

        self.assertEqual(get_joke(), 'hello world')

    @responses.activate
    def test_get_joke_raise_for_status(self):
        responses.get(
            url='http://api.icndb.com/jokes/random',
            json = {'value':{'joke':'hello world'}},
            status=403
        )

        self.assertEqual(get_joke(), 'HTTPError was raised')

    @responses.activate
    def test_get_joke_connection_error(self):
        responses.get(
            url='http://api.icndb.com/jokes/random',
            body=requests.ConnectionError('ConnectionError was raised')
        )

        self.assertEqual(get_joke(), 'ConnectionError was raised')

