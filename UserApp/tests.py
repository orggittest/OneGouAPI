from django.test import TestCase
import requests


# Create your tests here.
# 验证码测试
class User(TestCase):
    def test_user(self):
        url = 'http://127.0.0.1:8000/user/list/'
        resp = requests.get(url)
        return resp.json()

