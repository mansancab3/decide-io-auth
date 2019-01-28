from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .forms import FormSignUp,UserForm,ProfileForm
from django.contrib.auth import authenticate
from base import mods


class AuthTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        mods.mock_query(self.client)
        u = User(username='voter1')
        u.set_password('123')
        u.save()

    def tearDown(self):
        self.client = None

    def test_login(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)

        token = response.json()
        self.assertTrue(token.get('token'))

    def test_login_fail(self):
        data = {'username': 'voter1', 'password': '321'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_getuser(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 200)

        user = response.json()
        self.assertEqual(user['id'], 1)
        self.assertEqual(user['username'], 'voter1')

    def test_getuser_invented_token(self):
        token = {'token': 'invented'}
        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 404)

    def test_getuser_invalid_token(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.filter(user__username='voter1').count(), 1)

        token = response.json()
        self.assertTrue(token.get('token'))

        response = self.client.post('/authentication/logout/', token, format='json')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 404)

    def test_logout(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.filter(user__username='voter1').count(), 1)

        token = response.json()
        self.assertTrue(token.get('token'))

        response = self.client.post('/authentication/logout/', token, format='json')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Token.objects.filter(user__username='voter1').count(), 0)

    def test_newUser(self):
        data = {'username': 'username1', 'first_name': 'first_name1', 'last_name': 'last_name1','email': 'email1@gmail.com','sex': 'Hombre','location': 'location1','birth_date': '2018-01-28','password1': 'testnew1', 'password2': 'testnew1'}
        response = self.client.post('/authentication/createUser/', data, format='json')
        #Comprobamos que llegamos a la  vista
        self.assertEqual(response.status_code, 200)

        #Cargamos el formulario de la vista con los datos(data)
        form=FormSignUp(data)
        self.assertTrue(form)
        self.assertTrue(form.is_valid())
        form.save() #Guardamos al nuevo usuario

        #Comprobamos que el usuario existe realmente
        self.assertEqual(User.objects.filter(username='username1').count(), 1)

    def test_newUserRepeated(self):
        #Creamos el primer usuario
        data = {'username': 'username1', 'first_name': 'first_name1', 'last_name': 'last_name1','email': 'email1@gmail.com','sex': 'Hombre','location': 'location1','birth_date': '2018-01-28','password1': 'testnew1', 'password2': 'testnew1'}
        response = self.client.post('/authentication/createUser/', data, format='json')
        self.assertEqual(response.status_code, 200)
        form=FormSignUp(data)
        self.assertTrue(form.is_valid())
        form.save() #Guardamos al nuevo usuario 1
        self.assertEqual(User.objects.filter(username='username1').count(), 1) #Comprobamos que se guarda el primer usuario

        #Creamos el segundo usuario(con el mismo username)
        data2 = {'username': 'username1', 'first_name': 'first_name1', 'last_name': 'last_name2','email': 'email2@gmail.com','sex': 'Hombre','location': 'location1','birth_date': '2018-01-28','password1': 'testnew2', 'password2': 'testnew2'}
        response = self.client.post('/authentication/createUser/', data, format='json')
        self.assertEqual(response.status_code, 200)
        form=FormSignUp(data2)
        self.assertEqual(form.is_valid(),False)

         
    def test_newUserPassDifferent(self):
        #Creamos el primer usuario
        data = {'username': 'username1', 'first_name': 'first_name1', 'last_name': 'last_name1','email': 'email1@gmail.com','sex': 'Hombre','location': 'location1','birth_date': '2018-01-28','password1': 'testneaaw1', 'password2': 'testnew1'}
        response = self.client.post('/authentication/createUser/', data, format='json')
        self.assertEqual(response.status_code, 200)
        form=FormSignUp(data)
        self.assertEqual(form.is_valid(),False)


