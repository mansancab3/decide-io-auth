from django.http.response import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserCreationForm
from .serializers import UserSerializer
from django.shortcuts import render



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

def Inicio(request):
    formulario = UserCreationForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/admin')
    else:
        formulario =UserCreationForm()
    return render(request,'inicio.html',{"formUser":formulario})