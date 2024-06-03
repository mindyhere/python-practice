from chatbot.db.DatabaseConfig import *
from chatbot.db.Database import Database
from chatbot.Preprocess2 import Preprocess2

p = Preprocess2(word2index_dic='c:/work/python/pyweb2/FoodShop/chatbot/data/chatbot_dict.bin',
                userdic='c:/work/python/pyweb2/FoodShop/chatbot/data/user_dic.tsv')

db = Database(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME)
db.connect()

# 의도 파악
from chatbot.IntentModel import IntentModel
from chatbot.NerModel import NerModel
from chatbot.FindAnswer import FindAnswer

# 원문
items = ["오전에 탕수육 10개 주문합니다", "안녕하세요", "반가워요", "오늘 예약할께요", "군만두 주문할게요"]

for query in items:
    intent = IntentModel(model_name='c:/work/python/pyweb2/FoodShop/chatbot/model/intent_model.h5', proprocess=p)
    predict = intent.predict_class(query)
    intent_name = intent.labels[predict]

    # 개체명 인식
    ner = NerModel(model_name='c:/work/python/pyweb2/FoodShop/chatbot/model/ner_model.h5', proprocess=p)
    predicts = ner.predict(query)
    ner_tags = ner.predict_tags(query)
    print("질문 : ", query)
    print("=" * 100)
    print("의도 파악 : ", intent_name)
    print("개체명 인식 : ", predicts)
    print("답변 검색에 필요한 NER 태그 : ", ner_tags)
    print("=" * 100)

    # 답변 검색
    try:
        f = FindAnswer(db)
        answer_text, answer_image = f.search(intent_name, ner_tags)
        answer = f.tag_to_word(predicts, answer_text)

    except:
        answer = "죄송합니다. 질문을 이해하지 못했습니다."
    print("답변 : ", answer)
db.close()
