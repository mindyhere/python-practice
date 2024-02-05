from django.db import models


# Create your models here.
class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    question = models.TextField(null=False)
    # TextField → clob자료형
    # CharField → varchar2(4000byte)
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)
    status = models.CharField(max_length=1, default="y")


class Answer(models.Model):
    answer_idx = models.AutoField(primary_key=True)  # 응답일련번호
    survey_idx = models.IntegerField()  # 문제일련번호
    num = models.IntegerField()  # 선택값
