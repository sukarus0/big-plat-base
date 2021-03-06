# from django.test import TestCase
# from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status

# Create your tests here.
class masterTestCase(APITestCase):
    
    def setUp(self):
        self.client.post('/component/resource/', {'cpu': '1.0 vcpu', 'memory': '512 mb'}, format='json')
        self.client.post('/component/cluster_info/', {'component_type': 'kafka', 'number_of_members': 3}, format='json')
        return

    def test_get_resources(self):
        response = self.client.get('/component/resource/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cpu'], '1.0 vcpu')
        self.assertEqual(response.data['memory'], '512 mb')

    def test_get_cluster_info(self):
        response = self.client.get('/component/cluster_info/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['component_type'], 'kafka')
        self.assertEqual(response.data['number_of_members'], 3)
