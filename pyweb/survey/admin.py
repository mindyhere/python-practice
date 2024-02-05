from django.contrib import admin
from survey.models import Survey, Answer


# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
    # 관리자 화면 필드목록
    list_display = ("question", "ans1", "ans2", "ans3", "ans4", "status")


admin.site.register(Survey, SurveyAdmin)
#                   테이블     화면
admin.site.register(Answer)
