from django.shortcuts import render, redirect
from guestbook.models import Guestbook
from django.db.models import Q


# Create your views here.
def list(request):
    try:
        searchkey = request.POST['searchkey']
    except:
        searchkey = 'name' # 기본옵션

    try:
        search = request.POST['search']
    except:
        search = '' # 검색키워드

    if searchkey == 'name_content':
        # Q → 질의
        # Q(필드명__contains=키워드) ↔ 필드명 like '%키워드%' (: 검색기능 구현)                      정렬     - : 내림차순
        gbList = Guestbook.objects.filter(Q(name__contains=search) | Q(content__contains=search)).order_by('-idx')
    elif searchkey == 'name':
        gbList = Guestbook.objects.filter(Q(name__contains=search)).order_by('-idx')
    elif searchkey == 'content':
        gbList = Guestbook.objects.filter(Q(content__contains=search)).order_by('-idx')

    try:
        msg = request.GET['msg']
    except:
        msg = ''
    return render(request, "guestbook/list.html",
                  {"gbList": gbList, "gbCount": len(gbList), "searchkey": searchkey, "search": search, "msg": msg})


def write(request):
    return render(request, "guestbook/write.html")


def insert(request):
    row = Guestbook(name=request.POST['name'], email=request.POST['email'], passwd=request.POST['passwd'],
                    content=request.POST['content'])
    row.save()
    return redirect('/guestbook')


def passwd_check(request):
    id = request.POST['idx'] # 글번호
    pwd = request.POST['passwd'] # 비밀번호
    row = Guestbook.objects.get(idx=id)

    if row.passwd == pwd:
    #  실제비번      입력비번
        return render(request, "guestbook/edit.html", {'row': row})
    else:
        return redirect('/guestbook/?msg=error')


def update(request):
    id = request.POST['idx']
    pwd = request.POST['passwd']
    row = Guestbook.objects.get(idx=id)

    if row.passwd == pwd:
        row = Guestbook(idx=id, name=request.POST['name'], email=request.POST['email'], passwd=pwd,
                        content=request.POST['content'])
        row.save()
        return redirect('/guestbook')
    else:
        return redirect("/guestbook/?msg=error")


def delete(request):
    id = request.POST['idx']
    Guestbook.objects.get(idx=id).delete()
    return redirect('/guestbook')
