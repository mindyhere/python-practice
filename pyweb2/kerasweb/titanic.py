from flask import Flask, render_template, request
from keras.models import load_model
from joblib import load

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('titanic/input.html')


@app.route('/result', methods=['POST'])
def result():
    model = load_model('c:/data/titanic/titanic.keras')
    sex = request.form['sex']
    if sex == "male":
        male = 1
        female = 0
        gender = '남성'
    else:
        male = 0
        female = 1
        gender = '여성'

    pclass = request.form['pclass']
    if pclass == "1":
        pclass1 = 1
        pclass2 = 0
        pclass3 = 0
    elif pclass == "2":
        pclass1 = 0
        pclass2 = 1
        pclass3 = 0
    elif pclass == "3":
        pclass1 = 0
        pclass2 = 0
        pclass3 = 1

    age = int(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = float(request.form['fare'])

    test_set = [[pclass1, pclass2, pclass3, male, female, age, sibsp, parch, fare]]

    # 파일로 저장된 스케일러 로딩
    scaler = load('c:/data/titanic/scaler.model')

    # 테스트할 데이터를 스케일링 처리한 후 모형에 입력해야 함
    test_set = scaler.transform(test_set)
    rate = model.predict(test_set)

    if rate >= 0.5:
        result = '생존'
    else:
        result = '사망'

    return render_template('titanic/result.html', rate='{:.2f}%'.format(rate[0][0] * 100), result=result, sex=sex,
                           pclass=pclass, age=age, sibsp=sibsp, parch=parch, fare=fare)


if __name__ == '__main__':
    # http://127.0.0.1로 할 것
    app.run(port=8000, threaded=False)
