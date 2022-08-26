from unittest import TestCase
import requests
import random

cateid = ''
scateid = ''


class CategoryTest(TestCase):

    def test_01_getcategory(self):
        url = 'http://127.0.0.1:8000/fun/category/'
        num = random.randrange(1,3)
        cate = requests.get(url).json()
        global cateid
        cateid = cate['data'][num]['id']
        print(cate)
        print(cateid)


    def test_02_cate(self):
        global cateid
        global scateid
        url = 'http://127.0.0.1:8000/fun/catchild/?id='+cateid
        scate = requests.get(url).json()
        num = random.randrange(1, 3)
        scateid = scate['data'][num]['id']
        print(scate,cateid)
        print(cateid)


    def test_03_goods(self):
        global scateid
        url = 'http://127.0.0.1:8000/goods/getcate/?twoid='+scateid
        goods = requests.get(url).json()
        print(goods)




if __name__ == '__main__':
    CategoryTest().run()