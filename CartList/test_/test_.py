from unittest import TestCase

import requests
from django.http import request


class TestPost(TestCase):
    def test_1_down(self):
        url = 'http://localhost:8000/cart/orderdown/'
        data = {
            'order_num': 2,
            'goods_id': '0015d2a7-925a-4062-8958-e3b8a8ce568b',
            'address': '陕西省西安市雁塔区立人科技',
            'phone': '18693284019',
            'name': '魏凯强'
        }
        resp = requests.post(url, data=data)
        print(resp.text)

