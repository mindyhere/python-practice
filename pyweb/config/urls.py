from django.contrib import admin
from django.urls import path, include
from config import views

# url mapping 정보
urlpatterns = [
    path("admin/", admin.site.urls),
    # 관리자용 사이트

    path('', views.home),
    path('address/', include('address.urls')),
    # 모듈 : 확장자가 .py  →    패키지.모듈

    path("memo/", include("memo.urls")),
    # 한줄메모장 관련 url mapping

    path("book/", include("book.urls")),
    # 도서관리 관련 url mapping

    path("transaction/", include("transaction.urls")),
    # 트랜잭션 관련 url mapping

    path("procedure/", include("procedure.urls"))
    # 저장프로시저 관련 url mapping
]
