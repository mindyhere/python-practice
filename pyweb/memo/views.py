from django.shortcuts import render, redirect
from memo.models import Memo


# Create your views here.
def home(request):
    memoList = Memo.objects.order_by("-idx")
    return render(request, 'memo/list.html', {'memoList': memoList, 'memoCount': len(memoList)})


def insert_memo(request):
    memo = Memo(writer=request.POST['writer'], memo=request.POST['memo'])
    memo.save()
    return redirect("/memo")


def detail_memo(request):
    row = Memo.objects.get(idx=request.GET['idx'])
    return render(request, 'memo/detail.html', {'row': row})


def update_memo(request):
    memo = Memo(idx=request.POST['idx'],
                writer=request.POST['writer'],
                memo=request.POST['memo'])
    memo.save()
    return redirect("/memo")


def delete_memo(request):
    Memo.objects.get(idx=request.POST['idx']).delete()
    return redirect("/memo")
