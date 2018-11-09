import urllib.request
import json
import pytest
# import uuid
# import decimal


base_url = "http://localhost:5000/v1/system"
headers = {'Content-Type': 'application/json;charset=UTF-8'}

class TestSystem(object):

    def test_check_health_200(self):
        res = urllib.request.urlopen(base_url)
        data = str(res.read())

        assert "200" in data


    def test_check_system_200(self):
        res = urllib.request.urlopen(base_url + '?level=1')
        data = str(res.read())

        assert "200" in data
        assert "system" in data

