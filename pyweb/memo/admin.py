from django.contrib import admin
from memo.models import Memo


# admin.py →  models.py에 등록한 테이블이 Admin 사이트에서도 보이도록 처리

# Register your models here.
class MemoAdmin(admin.ModelAdmin):
    # 관리자 화면에서 관리할 필드 목록 정의
    list_display = ('writer', 'memo')


admin.site.register(Memo, MemoAdmin)
