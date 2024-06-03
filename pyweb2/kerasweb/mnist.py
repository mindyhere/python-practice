from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from keras.models import load_model

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('mnist/index.html')


@app.route('/uploader', methods=['POST'])
def upload_image():
    model = load_model('c:/data/mnist/mnist.h5')

    # 업로드한 파일을 gray scale로 변환
    img = Image.open(request.files['file'].stream).convert("L")
    print(type(img))

    # 업로드한 파일 사이즈가 mnist 이미지 size와 같도록 처리
    img = img.resize((28, 28))

    # 넘파이 배열로 변환
    arr = np.array(img) / 255
    print(arr.shape)

    # keras 모형에서 읽을 수 있도록 28x28에서 1x28x28x1로 차원 변경
    # 이미지개수x가로사이즈x세로사이즈x흑백(1)/컬러(3)
    arr = arr.reshape(1, 28, 28, 1)

    import tensorflow as tf
    with tf.device('/CPU:0'):
        pred = model.predict(arr)
        pred = np.argmax(pred, axis=1)
    return '숫자이미지: ' + str(pred[0])


if __name__ == '__main__':
    app.run(port=8000, threaded=False)
