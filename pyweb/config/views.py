from django.shortcuts import render


def home(request):
    # request 요청사항을 처리하는 객체

    # installed_app에 작성한 첫번째 앱인 address의 index.html 페이지로 출력됨
    return render(request, 'index.html')
    # retunr 화면이동
    # render : 'index.html' 템플릿 → 완성된 html (렌더링) + html페이지 포워드
