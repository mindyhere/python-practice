import pandas as pd
import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout, Conv1D, GlobalMaxPool1D, concatenate

gpus = tf.config.experimental.list_physical_devices('GPU')

if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

# 데이터 읽어오기
train_file = "c:/work/python/pyweb2/FoodShop/chatbot/data/total_train_data.csv"
data = pd.read_csv(train_file, delimiter=',')
queries = data['query'].tolist()
intents = data['intent'].tolist()

from chatbot.Preprocess2 import Preprocess2

p = Preprocess2(word2index_dic='c:/work/python/pyweb2/FoodShop/chatbot/data/chatbot_dict.bin',
                userdic='c:/work/python/pyweb2/FoodShop/chatbot/data/user_dic.tsv')

# 단어 시퀀스 생성
sequences = []

for sentence in queries:
    pos = p.pos(sentence)
    keywords = p.get_keywords(pos, without_tag=True)
    seq = p.get_wordidx_sequence(keywords)
    sequences.append(seq)

# 단어 인덱스 시퀀스 벡터
# 단어 시퀀스 벡터 크기

from chatbot.GlobalParams import MAX_SEQ_LEN

padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

# (105658, 15)
print(padded_seqs.shape)
print(len(intents))  # 105658

# 학습용, 검증용, 테스트용 데이터셋 생성
# 학습셋:검증셋:테스트셋 = 7:2:1
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, intents))
ds = ds.shuffle(len(queries))
train_size = int(len(padded_seqs) * 0.7)
val_size = int(len(padded_seqs) * 0.2)
test_size = int(len(padded_seqs) * 0.1)
train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).take(val_size).batch(20)
test_ds = ds.skip(train_size + val_size).take(test_size).batch(20)

# 하이퍼 파라미터 설정
dropout_prob = 0.5
EMB_SIZE = 128
EPOCH = 5
VOCAB_SIZE = len(p.word_index) + 1  # 전체 단어 개수

# CNN 모델 정의
input_layer = Input(shape=(MAX_SEQ_LEN,))
embedding_layer = Embedding(VOCAB_SIZE, EMB_SIZE, input_length=MAX_SEQ_LEN)(input_layer)
dropout_emb = Dropout(rate=dropout_prob)(embedding_layer)
conv1 = Conv1D(
    filters=128,
    kernel_size=3,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool1 = GlobalMaxPool1D()(conv1)
conv2 = Conv1D(
    filters=128,
    kernel_size=4,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool2 = GlobalMaxPool1D()(conv2)
conv3 = Conv1D(
    filters=128,
    kernel_size=5,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool3 = GlobalMaxPool1D()(conv3)

# 3,4,5gram 이후 합치기
concat = concatenate([pool1, pool2, pool3])
hidden = Dense(128, activation=tf.nn.relu)(concat)
dropout_hidden = Dropout(rate=dropout_prob)(hidden)
logits = Dense(5, name='logits')(dropout_hidden)
predictions = Dense(5, activation=tf.nn.softmax)(logits)

# 모델 생성
model = Model(inputs=input_layer, outputs=predictions)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습
with tf.device('/CPU:0'):
    model.fit(train_ds, validation_data=val_ds, epochs=EPOCH, verbose=1)

# 모델 평가(테스트 데이터 셋 이용)
with tf.device('/CPU:0'):
    loss, accuracy = model.evaluate(test_ds, verbose=1)
    print('Accuracy: %f' % (accuracy * 100))
    print('loss: %f' % (loss))

# 모델 저장
model.save('intent_model.h5')

print('완료되었습니다.')
