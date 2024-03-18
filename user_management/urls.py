from django.urls import path
from .views import *

app_name = 'user_management'


urlpatterns = [
    path('register-user', RegisterUser.as_view()),
    path('login-user', UserLogin.as_view()),
    path('zone-view', ZoneView.as_view())
]
