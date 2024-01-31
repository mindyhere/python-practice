from procedure import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('list_emp', views.list_emp),
    path('write_emp', views.write_emp),
    path('insert_emp', views.insert_emp),
    path('update_emp', views.update_emp),
    path('update_emp_p', views.update_emp_p),
    # path('list_memo_p', views.list_memo_p),
    # path('insert_memo_p', views.insert_memo_p),
    # path('view_memo_p', views.view_memo_p),
    # path('delete_memo_p', views.delete_memo_p),
    # path('update_memo_p', views.update_memo_p),
]
