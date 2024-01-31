from transaction import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('insert', views.insert),
    path('list', views.list),
]
