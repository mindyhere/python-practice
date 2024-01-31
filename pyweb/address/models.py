from django.db import models


# Create your models here.
# 이름, 전화, 이메일, 주소
class Address(models.Model):
    #        (상위 클래스)
    idx = models.AutoField(primary_key=True)
    # 변수명      .AutoField → 자동증가필드
    name = models.CharField(max_length=50, blank=True, null=True)
    #             vahchar    50             공백 허용   null 허용
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
