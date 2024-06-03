from flask import Flask, render_template, request
from keras.models import load_model
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('iris/input.html')


@app.route('/iris_result', methods=['POST'])
def iris_result():
    flowers = ['setosa', 'versicolor', 'virginica']
    model = load_model('c:/data/iris/iris.keras')
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])
    test_set = np.array([[a, b, c, d]])  # numpy배열(2차원배열)로
    pred = model.predict(test_set)
    print(pred)
    n = np.argmax(pred, axis=1)  # 최댓값의 인덱스 → 0번
    result = flowers[n[0]]
    return render_template('iris/iris_result.html', result=result, a=a, b=b, c=c, d=d)


if __name__ == '__main__':
    app.run(port=8000, threaded=False)
