from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import userAV

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('user/', userAV.as_view(), name='user')
]