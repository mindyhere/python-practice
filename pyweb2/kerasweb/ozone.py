from flask import Flask, render_template, request
from keras.models import load_model
import joblib

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('ozone/input.html')


@app.route('/result', methods=['POST'])
def result():
    model = load_model('c:/data/ozone/ozone.keras')
    scaler = joblib.load('c:/data/ozone/scaler.model')
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    test_set = [[a, b, c]]
    test_set = scaler.transform(test_set)
    rate = model.predict(test_set)

    if rate[0][0] >= 0.5:
        result = '충분'
    else:
        result = '부족'

    return render_template('ozone/result.html', rate='{:.2f}%'.format(rate[0][0] * 100), result=result, a=a, b=b, c=c)


if __name__ == '__main__':
    app.run(port=8000, threaded=False)
