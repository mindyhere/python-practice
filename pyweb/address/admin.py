from django.contrib import admin
from address.models import Address


# Register your models here.

# 화면에 출력할 필드목록을 튜플로 지정
# () 튜플 : 수정 불가
# [] 리스트 : 추가, 삭제 가능
class AddessAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'email', 'address')


admin.site.register(Address, AddessAdmin)
# 관리자 화면에 등록
