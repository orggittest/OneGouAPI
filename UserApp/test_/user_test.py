from unittest import TestCase
import requests


class Test_user(TestCase):
    def test_0_yzm(self):
        data = { 'yan': 'vwfMLh', 'phone': '17791692055', 'menu': 0}
        resp = requests.post(url='http://127.0.0.1:8000/user/list/', data=data)
        assert resp.json()['code'] == 200
        print(resp.json())

    def test_1_address(self):
        resp = requests.post(url='http://127.0.0.1:8000/user/address/', data={ 'menu': 0})
        assert resp.json()['code'] == 200
        print(resp.json()['msg'])

    def test_0_user_create(self):
        data = { 'phone': '12345678925', 'name': '不能少于八位，不能多余20位', }
        resp = requests.post('http://127.0.0.1:8000/user/list/')
        print(resp.json())
        return resp.json()

    def test_1__user_login(self):
        data = { 'yan': 'G313z7', 'phone': '17791692089', 'menu': '0'}
        resp = requests.post(url='http://127.0.0.1:8000/user/list/', data=data)
        print(resp.json()['code'])

    #def test_1_user_login(self):

if __name__ == '__main__':
    TestCase().run()