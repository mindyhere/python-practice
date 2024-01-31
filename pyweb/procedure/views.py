from django.shortcuts import render, redirect
from procedure.models import Emp
import oracledb


# Create your views here.

def home(request):
    return render(request, 'procedure/index.html')


def list_emp(request):
    empList = Emp.objects.order_by('ename')
    # Emp.objects → 테이블.objects : 모든 레코드
    return render(request, 'procedure/list_emp.html', {'empList': empList, 'empCount': len(empList)})


def update_emp(request):
    emp = Emp.objects.get(empno=request.GET['empno'])
    sal = int(request.GET['sal']) * 1.1

    # 객체 생성
    emp_new = Emp(empno=emp.empno, ename=emp.ename, job=emp.job, hiredate=emp.hiredate, sal=sal)
    # 업데이트 실행
    emp_new.save()
    return redirect('/procedure/list_emp')


def update_emp_p(request):
    try:
        # with 문장 → with 블록이 종료됐을 때, 메모리 AUTO close
        # OracleDB 접속
        with oracledb.connect("python/1234@localhost:1521/xe") as conn:
            with conn.cursor() as cursor:
                empno = request.GET['empno']
                cursor.callproc('mysal_p', [empno])
                #                프로시저 호출     매개변수
                conn.commit()
    except Exception as e:
        print(e)

    return redirect('/procedure/list_emp')


def write_emp(request):
    return render(request, 'procedure/write_emp.html')


def insert_emp(request):
    emp = Emp(empno=request.POST['empno'], ename=request.POST['ename'], job=request.POST['job'],
              hiredate=request.POST['hiredate'], sal=request.POST['sal'])
    emp.save()
    return redirect('/procedure/list_emp')
