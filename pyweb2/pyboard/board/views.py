import math
import os
from django.shortcuts import redirect, render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from board.models import Board, Comment
from urllib.parse import quote

# Create your views here.
UPLOAD_DIR = "c:/upload/"


def list(request):
    try:
        search_option = request.POST["search_option"]
    except:
        search_option = "writer"

    try:
        search = request.POST["search"]
    except:
        search = ""

    boardCount = Board.objects.count()

    try:
        start = int(request.GET['start'])
    except:
        start = 0

    page_size = 10  # 페이지당 게시물수
    page_list_size = 10  # 한 화면에 표시할 페이지 개수
    end = start + page_size
    total_page = math.ceil(boardCount / page_size)
    current_page = math.ceil((start + 1) / page_size)
    start_page = math.floor((current_page - 1) / page_list_size) * page_list_size + 1
    end_page = start_page + page_list_size - 1

    if total_page < end_page:
        end_page = total_page
    if start_page >= page_list_size:
        prev_list = (start_page - 2) * page_size
    else:
        prev_list = 0

    if total_page > end_page:
        next_list = end_page * page_size
    else:
        next_list = 0

    if search_option == "all":
        boardList = Board.objects.filter(
            Q(writer__contains=search) | Q(title__contains=search) | Q(content__contains=search)).order_by("-idx")[
                    start:end]
    elif search_option == "writer":
        boardList = Board.objects.filter(writer__contains=search).order_by("-idx")[start:end]
    elif search_option == "title":
        boardList = Board.objects.filter(title__contains=search).order_by("-idx")[start:end]
    elif search_option == "content":
        boardList = Board.objects.filter(content__contains=search).order_by("-idx")[start:end]

    links = []
    for i in range(start_page, end_page + 1):
        page = (i - 1) * page_size
        links.append("<a href='?start=" + str(page) + "'>" + str(i) + "</a>")

    return render(request, "list.html", {"boardList": boardList, "search_option": search_option, "search": search,
                                         "range": range(start_page - 1, end_page), "start_page": start_page,
                                         "end_page": end_page, "page_list_size": page_list_size,
                                         "total_page": total_page, "prev_list": prev_list, "next_list": next_list,
                                         "links": links})


def write(request):
    return render(request, "write.html")


def insert(request):
    fname = ""
    fsize = 0
    if "file" in request.FILES:
        file = request.FILES["file"]
        fname = file._name

        with open("%s%s" % (UPLOAD_DIR, fname), 'wb') as fp:
            for chunk in file.chunks():
                fp.write(chunk)

        fsize = os.path.getsize(UPLOAD_DIR + fname)

    row = Board(writer=request.POST["writer"], title=request.POST["title"], content=request.POST["content"],
                filename=fname, filesize=fsize)
    row.save()

    return redirect("/")


def detail(request):
    # 조회수 증가 처리
    id = request.GET["idx"]
    row = Board.objects.get(idx=id)
    row.hit_up()
    row.save()

    commentList = Comment.objects.filter(board_idx=id).order_by("idx")

    filesize = "%.2f" % (row.filesize / 1024)
    return render(request, "detail.html", {"row": row, "filesize": filesize, "commentList": commentList})


def update(request):
    id = request.POST['idx']
    row_src = Board.objects.get(idx=id)

    fname = row_src.filename  # 수정 전의 첨부파일 이름
    fsize = row_src.filesize  # 수정 전의 첨부파일 크기
    hit = row_src.hit  # 수정 전의 조회수
    down = row_src.down  # 수정 전의 다운로드 횟수

    if "file" in request.FILES:
        file = request.FILES["file"]
        fname = file._name

        with open("%s%s" % (UPLOAD_DIR, fname), 'wb') as fp:
            for chunk in file.chunks():
                fp.write(chunk)

        fsize = os.path.getsize(UPLOAD_DIR + fname)

        row_new = Board(idx=id, writer=request.POST["writer"], title=request.POST["title"],
                        content=request.POST["content"], filename=fname, filesize=fsize, hit=hit, down=down)
        row_new.save()
        return redirect("/")


def delete(request):
    id = request.POST["idx"]
    Board.objects.get(idx=id).delete()
    return redirect("/")


def download(request):
    id = request.GET['idx']
    row = Board.objects.get(idx=id)
    path = UPLOAD_DIR + row.filename

    filename = os.path.basename(path)
    filename = quote(filename)

    with open(path, 'rb') as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response["Content-Disposition"] = "attachment; filename*=UTF-8''{0}".format(filename)
        row.down_up()
        row.save()
        return response


def reply_insert(request):
    id = request.POST['idx']
    row = Comment(board_idx=id, writer=request.POST["writer"], content=request.POST["content"])

    row.save()
    return HttpResponseRedirect("detail?idx=" + id)
