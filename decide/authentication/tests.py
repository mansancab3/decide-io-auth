from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


from .forms import FormSignUp,UserForm,ProfileForm
from django.contrib.auth import authenticate
from base import mods
import urllib.request, urllib.error

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

        #Test login facebook and google


    def test_request_facebook(self):
        try:
            request = urllib.request.urlopen('https://www.facebook.com/login.php?skip_api_login=1&api_key=803345486672646&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fredirect_uri%3Dhttp%253A%252F%252Flocalhost%253A8000%252Faccounts%252Ffacebook%252Flogin%252Fcallback%252F%26state%3DneYAaUWIcobc%26scope%26response_type%3Dcode%26client_id%3D803345486672646%26ret%3Dlogin%26logger_id%3D2ce173ff-0037-d09b-ce8f-6816a7547584&cancel_url=http%3A%2F%2Flocalhost%3A8000%2Faccounts%2Ffacebook%2Flogin%2Fcallback%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DneYAaUWIcobc%23_%3D_&display=page&locale=es_ES&logger_id=2ce173ff-0037-d09b-ce8f-6816a7547584')
        except urllib.error.HTTPError as errors:
            self.assertEqual(errors.code, 400) 
            self.assertEqual(errors.code, 403) 
            self.assertEqual(errors.code, 404)

    def test_request_googleLogin(self):
        try:
            request = urllib.request.urlopen('https://accounts.google.com/signin/oauth/oauthchooseaccount?client_id=1096255128002-nbae62sdmoo0v19ugua198ou30coht1s.apps.googleusercontent.com&as=CdsB_y45brgqlnQURWSiQg&destination=http%3A%2F%2Flocalhost%3A8000&approval_state=!ChQyWDVxdU9lcGs2c3d1VVRubEFwVRIfMDIteU9qNTY5cThRMEVBN1JaNXdOM005V3dZVmlSWQ%E2%88%99APNbktkAAAAAXE96j6wpjQrJA5CJm4K7si5nr3IfoMe8&oauthgdpr=1&xsrfsig=ChkAeAh8TyABjjbCCFJMcA-mTBaDlLhdg-rtEg5hcHByb3ZhbF9zdGF0ZRILZGVzdGluYXRpb24SBXNvYWN1Eg9vYXV0aHJpc2t5c2NvcGU&flowName=GeneralOAuthFlow')
        except urllib.error.HTTPError as errors:
            self.assertEqual(errors.code, 400) 

    def test_newUser(self):
        data = {'username': 'username1', 'first_name': 'first_name1', 'last_name': 'last_name1','email': 'email1@gmail.com','sex': 'MAN','location': 'location1','birth_date': '2018-01-28','password1': 'testnew1', 'password2': 'testnew1'}
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
        data = {'username': 'username1', 'first_name': 'first_name1', 'last_name': 'last_name1','email': 'email1@gmail.com','sex': 'MAN','location': 'location1','birth_date': '2018-01-28','password1': 'testnew1', 'password2': 'testnew1'}
        response = self.client.post('/authentication/createUser/', data, format='json')
        self.assertEqual(response.status_code, 200)
        form=FormSignUp(data)
        self.assertTrue(form.is_valid())
        form.save() #Guardamos al nuevo usuario 1
        self.assertEqual(User.objects.filter(username='username1').count(), 1) #Comprobamos que se guarda el primer usuario

        #Creamos el segundo usuario(con el mismo username)
        data2 = {'username': 'username1', 'first_name': 'first_name1', 'last_name': 'last_name2','email': 'email2@gmail.com','sex': 'MAN','location': 'location1','birth_date': '2018-01-28','password1': 'testnew2', 'password2': 'testnew2'}
        response = self.client.post('/authentication/createUser/', data, format='json')
        self.assertEqual(response.status_code, 200)
        form=FormSignUp(data2)
        self.assertEqual(form.is_valid(),False)

         
    def test_newUserPassDifferent(self):
        #Creamos el primer usuario
        data = {'username': 'username1', 'first_name': 'first_name1', 'last_name': 'last_name1','email': 'email1@gmail.com','sex': 'MAN','location': 'location1','birth_date': '2018-01-28','password1': 'testneaaw1', 'password2': 'testnew1'}
        response = self.client.post('/authentication/createUser/', data, format='json')
        self.assertEqual(response.status_code, 200)
        form=FormSignUp(data)
        self.assertEqual(form.is_valid(),False)


