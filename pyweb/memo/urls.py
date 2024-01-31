from memo import views
from django.urls import path

urlpatterns = [
    # 한줄메모장 관련 url
    path('', views.home),
    path('insert_memo', views.insert_memo),
    path('detail', views.detail_memo),
    path('update_memo', views.update_memo),
    path('delete_memo', views.delete_memo),
]
