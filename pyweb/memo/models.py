from datetime import datetime
from django.db import models


# models.py → 테이블에 대한 모델클래스 정의
# 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은 클래스의 변수로 매핑
# 테이블 클래스는 django.db.models.Model 클래스를 상속받아 정의함
# 변수 자료형 : jango에서 미리 정의된 자료형을 사용함

# Create your models here.
# 테이블과의 매핑을 위한 클래스
class Memo(models.Model):
    # 필드 = 자료형.속성
    idx = models.AutoField(primary_key=True)  # 자동증가, PK
    writer = models.CharField(max_length=50, blank=True, null=True)
    memo = models.CharField(max_length=2000, blank=True, null=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)  # 날짜 - 현재 시각으로 자동 입력
