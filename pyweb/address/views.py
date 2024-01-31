from django.shortcuts import redirect, render
from address.models import Address


# Create your views here.
def home(request):
    items = Address.objects.order_by("name")
    # Address.objects : 모든 레코드
    return render(request, 'address/list.html', {'items': items, 'address_count': len(items)})


def write(request):
    return render(request, "address/write.html")


def insert(request):
    addr = Address(name=request.POST['name'], tel=request.POST['tel'], email=request.POST['email'],
                   address=request.POST['address'])
    addr.save()  # DB insert 쿼리 실행
    return redirect('/address/')


def detail(request):
    addr = Address.objects.get(idx=request.GET['idx'])
    return render(request, 'address/detail.html', {'addr': addr})


def update(request):
    addr = Address(idx=request.POST['idx'], name=request.POST['name'], tel=request.POST['tel'],
                   email=request.POST['email'], address=request.POST['address'])
    addr.save() # DB update 쿼리 실행
    return redirect('/address/')


def delete(request):
    Address.objects.get(idx=request.POST['idx']).delete()
    # 폼(post 방식)에서 submit → request.POST['idx']
    return redirect('/address/')
