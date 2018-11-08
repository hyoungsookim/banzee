import urllib.request
import json
import pytest
# import uuid
# import decimal

#from server.models.partner import Partner


base_url = "http://localhost:5000/v1/partners"
headers = {'Content-Type': 'application/json;charset=UTF-8'}

class TestPartnerData(object):

    def test_get_list_200(self):
        res = urllib.request.urlopen(base_url)
        data = str(res.read())

        assert "200" in data
        assert "partners" in data

    def test_get_200(self):
        res = urllib.request.urlopen(base_url + '/VINCLE')
        data = str(res.read())

        assert "200" in data
        assert "partner" in data

    def test_create_200(self):
        data = '{ \
                    "partner_id": "TEST_PARTNER", \
                    "partner_name": "test partner", \
                    "partner_status": 200 \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='POST')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        #partner_id = json.loads(data).get('partner').get('partner_id')

        assert "200" in data
        assert "partner" in data

    def test_update_200(self):
        data = '{ \
                    "partner_status": 0, \
                    "partner_name": "Partner" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url + '/TEST_PARTNER', 
                                    data=data,
                                    headers=headers,
                                    method='PUT')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "partner_id" in data


    def test_delete_200(self):
        req = urllib.request.Request(base_url + '/TEST_PARTNER',
                                    headers=headers,
                                    method='DELETE')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data

