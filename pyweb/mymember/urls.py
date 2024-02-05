from django.urls import path
from mymember import views

urlpatterns = [
    path('', views.home),
    path('join', views.join),
    path('login', views.login),
    path('logout', views.logout),
]
