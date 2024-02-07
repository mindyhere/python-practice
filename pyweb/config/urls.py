from django.contrib import admin
from django.urls import path, include
from config import views
from django.conf import settings
from django.urls import re_path

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

    path("procedure/", include("procedure.urls")),
    # 저장프로시저 관련 url mapping

    path("mymember/", include("mymember.urls")),
    # 회원관리 관련 url mapping

    path("ajax/", include("ajax.urls")),
    # Ajax실습 관련 url mapping

    path("survey/", include("survey.urls")),
    # 설문조사 실습 관련 url mapping

    path("guestbook/", include("guestbook.urls")),
    # 방명록 실습 관련 url mapping

    path("shop/", include("shop.urls")),
    # 상품관리 실습 관련 url mapping
]

if settings.DEBUG:  # → true=개발중
    import debug_toolbar

    urlpatterns += [
        re_path(r'^__debug__', include(debug_toolbar.urls)),  # re_path → 정규표현식(regular expression)
    ]
