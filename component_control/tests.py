# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.views import status

# Create your tests here.
class componentControlTestCase(APITestCase):

    def setUp(self):
        self.client.post('/component-control/info/', {'name': 'kafka', 'status': 'running'}, format='json')
        self.client.post('/component-control/info/', {'name': 'hdfs', 'status': 'running'}, format='json')
        self.client.post('/component-control/info/', {'name': 'spark', 'status': 'pending'}, format='json')

    def test_get_component_control_info(self):
        response = self.client.get('/component-control/info/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'kafka')
        self.assertEqual(response.data['status'], 'running')

        response = self.client.get('/component-control/info/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'hdfs')
        self.assertEqual(response.data['status'], 'running')
        
        response = self.client.get('/component-control/info/3/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'spark')
        self.assertEqual(response.data['status'], 'pending')
