from django.shortcuts import render, redirect
from shop.models import Member, Chat
import hashlib
from shop.mychatbot import getMessage


def home(request):
    if 'userid' not in request.session.keys():
        return render(request, 'shop/login.html')
    else:
        return render(request, 'shop/main.html')


def login(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        passwd = request.POST['passwd']
        passwd = hashlib.sha256(passwd.encode()).hexdigest()
        row = Member.objects.filter(userid=userid, passwd=passwd)

        if len(row) > 0:
            row = Member.objects.filter(userid=userid, passwd=passwd)[0]
            request.session['userid'] = userid
            request.session['name'] = row.name
            return render(request, 'shop/main.html')

        else:
            return render(request, 'shop/login.html',
                          {'msg': '아이디 또는 비밀번호가 일치하지 않습니다.'})

    else:
        return render(request, 'shop/login.html')


def join(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        passwd = request.POST['passwd']
        passwd = hashlib.sha256(passwd.encode()).hexdigest()
        name = request.POST['name']
        address = request.POST['address']
        tel = request.POST['tel']

        Member(userid=userid, passwd=passwd, name=name, address=address, tel=tel).save()

        request.session['userid'] = userid
        request.session['name'] = name

        return render(request, 'shop/main.html')

    else:
        return render(request, 'shop/join.html')


def logout(request):
    request.session.clear()
    return redirect('/')


def order(request):
    return render(request, 'shop/order.html')


def query(request):
    question = request.GET["question"]
    msg = getMessage(question)
    query = msg['Query']
    answer = msg['Answer']
    intent = msg['Intent']
    Chat(userid=request.session['userid'], query=query, intent=intent).save()
    Chat(userid=request.session['userid'], answer=answer, intent=intent).save()
    items = Chat.objects.filter(userid=request.session['userid']).order_by('-idx')
    return render(request, 'shop/result.html', {'items': items})


def delete_chat(request):
    Chat.objects.filter(userid=request.session['userid']).delete()
    return redirect('/order')
