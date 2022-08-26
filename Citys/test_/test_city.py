import requests
import unittest
from unittest import TestCase

import random


test_data = {

}


class CityTestCase(TestCase):
    def test_01_all_city(self):
        url = 'http://localhost:8000/city/all'
        resp = requests.get(url)
        city_list = resp.json().get('data')

        city = random.choice(city_list)

        test_data['city_id'] = city['id']
        print('------定位当前的城市-------', city['city_name'], test_data['city_id'])

    def test_02_city_area(self):
        url = 'http://localhost:8000/city/area/'
        resp = requests.get(url, {
            'one_id': test_data['city_id']
        })

        area_list = resp.json().get('data')

        area = random.choice(area_list)

        print('-------定位的区县-----------', area['cityareaname'])

        self.area_id = area['id']


if __name__ == '__main__':
    unittest.main()



