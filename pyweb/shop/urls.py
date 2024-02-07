from django.urls import path
from shop import views

urlpatterns = [
    # 상품관련
    path('product_list', views.product_list),
    path('product_write', views.product_write),
    path('product_insert', views.product_insert),
    path('product_detail', views.product_detail),
    path('product_edit', views.product_edit),
    path('product_update', views.product_update),
    path('product_delete', views.product_delete),

    # 장바구니 관련
    path('cart_insert', views.cart_insert),
    path('cart_list', views.cart_list),
    path('cart_update', views.cart_update),
    path('cart_del', views.cart_del),
    path('cart_del_all', views.cart_del_all),
]
