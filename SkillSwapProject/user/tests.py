from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from rest_framework import status
from .models import User
import jwt
class UserRegister(TestCase):

    

    def setUp(self):
        self.client = APIClient()

    def test_user_register(self):
       
        data = {"username":"nithisha1","password":"1234","email":"gnithisha5k4@gmail.com","phone_number":"+919392380582","first_name":"gujja","last_name":"nithisha"}
        response = self.client.post('/userregister/',data=data,headers ={})
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_user_with_null_fields(self):
        data = {"username":"nithisha1","password":"1234","email":"gnithisha5k4@gmail.com","phone_number":"+919392380582"}
        response = self.client.post("/userregister/",data=data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_user_with_existing_username(self):
        data = {"username":"nithisha1","password":"1234","email":"gnithisha5k4@gmail.com","phone_number":"+919392380582","first_name":"gujja","last_name":"nithisha"}
        data1 = {"username":"nithisha1","password":"1234"}
        User.objects.create_user(**data)
        response = self.client.post('/userregister/',data=data1)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    
    def test_user_with_existing_email(self):
        data = {"username":"nithisha1","password":"1234","email":"gnithisha5k4@gmail.com","phone_number":"+919392380582","first_name":"gujja","last_name":"nithisha"}
        data1 = {"username":"nithisha3","password":"12345","email":"gnithisha5k4@gmail.com"}
        User.objects.create_user(**data)
        response = self.client.post('/userregister/',data=data1)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

class UserLoginTests(APITestCase):
    def setUp(self):
        self.url = '/login/'  # Replace 'login' with the actual name of your URL pattern
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.secret = 'abcd'
        self.algorithm = 'HS256'

    def test_login_with_valid_credentials(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

        # Decode and verify the token
        token = response.data['token']
        payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        self.assertEqual(payload['user_id'], self.user.id)
        self.assertTrue('exp' in payload)
        self.assertTrue(payload['exp'] > datetime.utcnow().timestamp())

    def test_login_with_invalid_credentials(self):
        data = {
            'username': self.username,
            'password': 'wrongpassword'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_login_with_empty_credentials(self):
        data = {
            'username': '',
            'password': ''
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

from .models import Data  # Replace with actual import path
from .serializers import DataSerializer  # Replace with actual import path

class UserDataViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.data1 = Data.objects.create(name='Data 1', age=12)
        self.data2 = Data.objects.create(name='Data 2', age=11)

    def test_get_all_data(self):
        response = self.client.get('/data/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = DataSerializer([self.data1, self.data2], many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_get_single_data(self):
        response = self.client.get(f'/data/{self.data1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = DataSerializer(self.data1).data
        self.assertEqual(response.data, serializer_data)

    def test_create_data(self):
        new_data = {'name': 'New Data', 'age':12}
        response = self.client.post('/data/', new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Data.objects.count(), 3)  # Assuming there are already 2 data objects

    def test_update_data(self):
        updated_data = {'name': 'Updated Data', 'age': 1}
        response = self.client.put(f'/data/{self.data1.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.data1.refresh_from_db()
        self.assertEqual(self.data1.name, 'Updated Data')

    def test_delete_data(self):
        response = self.client.delete(f'/data/{self.data1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Data.objects.filter(id=self.data1.id).exists())

    def test_unauthenticated_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/data/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    


    
    


