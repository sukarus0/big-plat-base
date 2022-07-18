# from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status

# Create your tests here.
class masterTestCase(APITestCase):
    
    def setUp(self):
        data = [
            {'category': '수집', 'name': 'kafka', 'access_point': 'http://kafka.service'},
            {'category': '저장', 'name': 'hdfs', 'access_point': 'http://hdfs.service'},
            {'category': '처리', 'name': 'spark', 'access_point': 'http://spark.service'},
        ]
        self.client.post('/master/', data=data[0], format='json')
        self.client.post('/master/', data=data[1], format='json')
        self.client.post('/master/', data=data[2], format='json')

    def test_get_big_data_components_list(self):
        response = self.client.get('/master/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0].keys()), 3)

    def test_get_first_big_data_component(self):
        response = self.client.get('/master/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], '수집')
        self.assertEqual(response.data['name'], 'kafka')
        self.assertEqual(response.data['access_point'], 'http://kafka.service')

        response = self.client.get('/master/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], '저장')
        self.assertEqual(response.data['name'], 'hdfs')
        self.assertEqual(response.data['access_point'], 'http://hdfs.service')

        response = self.client.get('/master/3/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], '처리')
        self.assertEqual(response.data['name'], 'spark')
        self.assertEqual(response.data['access_point'], 'http://spark.service')
