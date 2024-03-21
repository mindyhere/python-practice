from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('iris/input.html')


@app.route('/iris_result', methods=['POST'])
def iris_result():
    flowers = ['setosa', 'versicolor', 'virginica']
    model = joblib.load('c:/data/iris/iris_logit.model')
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])

    test_set = [[a, b, c, d]]
    n = model.predict(test_set)
    result = flowers[n[0]]
    return render_template('iris/result.html', result=result, a=a, b=b, c=c, d=d)


if __name__ == '__main__':
    app.run(port=8000, threaded=False)
