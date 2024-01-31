from django.db import models


# Create your models here.
# 테이블이름 → 앱_클래스명(소문자)
# transaction_emp
class Emp(models.Model):
    # 필드  자료형
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50, null=False)  # ↔ varchar(50)
    deptno = models.IntegerField(null=False)
