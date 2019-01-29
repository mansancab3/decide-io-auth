from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from .views import GetUserView, LogoutView,EditUser,CreateUser,LoginUser, LogoutUser, ChangePassUser


urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('getuser/', GetUserView.as_view()),
    path('loginUser/', LoginUser.as_view()),
    path('logoutUser/', LogoutUser),
    path('editUser/', EditUser),
    path('createUser/', CreateUser),
    path('changePassUser/', ChangePassUser),
]
