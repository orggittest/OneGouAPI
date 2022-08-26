from unittest import TestCase

import requests
from django.http import request


class TestPost(TestCase):
    def test_post(self):
        url = 'http://localhost:8000/goods/gethome/'
        resp = requests.post(url)
        # self.assertEqual(resp.status_code, 200, '请求失败')

        print(resp)
        print(resp.text)

class TestGet(TestCase):
    def test_1_post(self):
        url = 'http://localhost:8000/goods/getcate/?oneid=ad7f227d-73c0-44a2-9edd-924006deb134'
        resp = requests.get(url)

        print(resp.text)

class TestCode(TestCase):
    def test_1_post(self):
        url = 'http://localhost:8000/goods/getinfo/?goods_code=6000036238'

        resp = requests.post(url)

        print(resp.text)