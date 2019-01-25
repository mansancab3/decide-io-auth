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

from .serializers import UserSerializer
from .forms import ProfileForm,UserForm,FormSignUp


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


#Anadido por Decide-IO-Auth
def EditUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
        	user_form.save()
        	profile_form.save()
        	return HttpResponseRedirect('/admin')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'editUser.html', {"userForm":user_form,'profileForm': profile_form})

class CreateUser(CreateView):
    template_name = 'createUser.html'
    model = Profile
    form_class = FormSignUp

    def form_valid(self, form):
        form.save()
		#Una vez nos registramos automaticamentes nos logeamos y entramos en nuestra vista de usuario
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class LoginUser(LoginView):
    template_name = 'login.html'

class LogoutUser(LogoutView):
    pass



