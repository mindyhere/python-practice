from django.urls import path
from ajax import views

urlpatterns = [
    path('', views.home),
    path('gugu', views.gugu),
    path('gugu_ajax', views.gugu_ajax),
    path('login', views.login),
    path('login_check', views.login_check),
    path('keyword', views.keyword),
    path('keyword_list', views.keyword_list),
    path('logout', views.logout),
]
