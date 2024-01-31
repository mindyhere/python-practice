from django.shortcuts import render, redirect
from django.template.context_processors import request

from book.models import Book


# Create your views here.

def list(request):
    bookList = Book.objects.order_by('-idx')
    return render(request, 'book/list.html', {'bookList': bookList, 'bookCount': len(bookList)})


def write(request):
    return render(request, 'book/write.html')


def insert(request):
    book = Book(title=request.POST['title'], author=request.POST['author'], price=int(request.POST['price']),
                amount=int(request.POST['amount']))
    book.save()
    return redirect('/book')


def edit(request):
    row = Book.objects.get(idx=request.GET['idx'])
    return render(request, 'book/edit.html', {'row': row})


def update(request):
    book = Book(idx=request.POST['idx'], title=request.POST['title'], author=request.POST['author'],
                price=int(request.POST['price']), amount=int(request.POST['amount']))
    book.save()
    return redirect('/book')


def delete(request):
    Book.objects.get(idx=request.POST['idx']).delete()
    return redirect('/book')
