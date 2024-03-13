from flask import Flask, Markup, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])  # URL패턴
def main():  # 시작페이지 호출 함수
    return render_template('gugu.html')


@app.route('/gugu_result', methods=['POST'])
def gugu_result():
    dan = int(request.form['dan'])
    result = ''

    for i in range(1, 10):
        result += f'{dan} X {i} = {dan * i}<br>'  # f'{변수}' → format string

    result = Markup(result)  # html 태그(<br>태그)를 인식하게 하는 함수
    return render_template('gugu_result.html', result=result)


if __name__ == '__main__':
#  실행파일      현재파일
# __변수__ → 시스템변수
    # threaded를 True로 설정하면 신경망 모형을 불러오는 코드에서 에러가 발생하므로 False로 설정
    # multithread off(순서대로 처리함)
    app.run(port=8000, threaded=False)
