import time
from django.db import transaction
from django.shortcuts import render
from transaction.models import Emp


# Create your views here.
def home(request):
    return render(request, 'transaction/index.html')


# 함수 트랜잭션 설정
# @transaction.atomic()
# 오류발생 → rollback / 오류X → commit
def insert(request):
    start = time.time()  # 현재시간
    Emp.objects.all().delete()  # 모든 레코드 삭제 (→ delete from transaction_emp;)

    for i in range(1, 1001):
        #     if i == 500:
        #         emp = Emp(empno='500번', ename='name' + str(i), deptno=i)  # 에러를 발생시키는 코드
        #         emp.save()
        #     else:
        emp = Emp(empno=i, ename='name' + str(i), deptno=i)
        emp.save()
    end = time.time()
    runtime = end - start
    cnt = Emp.objects.count()
    return render(request, 'transaction/index.html', {'cnt': cnt, 'runtime': f'{runtime:.2f}초'})


def list(request):
    empList = Emp.objects.all().order_by('empno')
    return render(request, 'transaction/list.html', {'empList': empList, 'empCount': len(empList)})
