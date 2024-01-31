from django.db import models
from datetime import datetime


# Create your models here.
class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50, null=False)
    job = models.CharField(max_length=50, null=False)
    hiredate = models.DateTimeField(default=datetime.now)
    sal = models.IntegerField(null=False, default=0)

    # 함수 선언
    # def 함수이름(self, 매개변수): 실행코드
    def update_sal(self, sal):
        self.sal = sal
