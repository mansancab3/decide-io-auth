from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .models import Profile


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import json
import requests
from django.conf import settings
from django.contrib import messages
from .serializers import UserSerializer
from .forms import ProfileForm,UserForm,FormSignUp
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.contrib.auth import logout


class GetUserView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        tk = get_object_or_404(Token, key=key)
        return Response(UserSerializer(tk.user, many=False).data)


class LogoutView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        try:
            tk = Token.objects.get(key=key)
            tk.delete()
        except ObjectDoesNotExist:
            pass

        return Response({})


#--------------------------Anadido por Decide-IO-Auth -----------------------------------

def EditUser(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return HttpResponseRedirect('/index')
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)

        return render(request, 'editUser.html', {"userForm":user_form,'profileForm': profile_form})
    else:
        return HttpResponseRedirect('/')

def ChangePassUser(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been modified correctly')
            return redirect('/index')
        else:
            messages.error(request, 'An error occurred when changing the password, please check it')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changePassUser.html', {'form': form})

def UseCapcha(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = r.json()
    return result

def CreateUser(request):
    if request.method == 'POST':
        form = FormSignUp(request.POST)
        if form.is_valid():
            #Se carga los datos del capcha
            result = UseCapcha(request)

            if result['success']:
                user = form.save()
                user.refresh_from_db()
                user.profile.sex = form.cleaned_data.get('sex')
                user.profile.location = form.cleaned_data.get('location')
                user.profile.birth_date = form.cleaned_data.get('birth_date')
                user.save()

                #Se manda correo para informar de que se ha registrado en Decide
                email = form.cleaned_data.get('email')
                send_mail('Record app Decide','Successfully registered in the Decide-IO application. From now on you can vote in all our votes. If you have not registered, contact the email that sent you this message','decideio@hotmail.com',[email])
                ################################################################

                password = form.cleaned_data.get('password1')
                usuario = authenticate(username=user.username, password=password)
                login(request, usuario)
                return HttpResponseRedirect('/authentication/editUser')
            else:
                print("Captcha not passed, try again")
                messages.add_message(request, messages.ERROR, 'Captcha not passed, try again')
    else:
        form = FormSignUp()

    return render(request, 'createUser.html', {"form":form})


class LoginUser(LoginView):
    template_name = 'login.html'

def LogoutUser(request):
    logout(request)
    return redirect('/authentication/loginUser')

class IndexPage(TemplateView):
    template_name = 'index.html'
