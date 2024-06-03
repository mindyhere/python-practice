from chatbot.db.DatabaseConfig import *
from chatbot.db.Database import Database
from chatbot.Preprocess2 import Preprocess2
from chatbot.IntentModel import IntentModel
from chatbot.NerModel import NerModel
from chatbot.FindAnswer import FindAnswer

# 전처리 객체 생성

p = Preprocess2(word2index_dic='c:/work/python/pyweb2/FoodShop/chatbot/data/chatbot_dict.bin',
                userdic='c:/work/python/pyweb2/FoodShop/chatbot/data/user_dic.tsv')

# 의도 파악 모델
intent = IntentModel(model_name='c:/work/python/pyweb2/FoodShop/chatbot/model/intent_model.h5', proprocess=p)

# 개체명 인식 모델
ner = NerModel(model_name='c:/work/python/pyweb2/FoodShop/chatbot/model/ner_model.h5', proprocess=p)

def getMessage(query):
    try:
        db = Database(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
        )
        db.connect()

        # 의도 파악
        intent_predict = intent.predict_class(query)
        intent_name = intent.labels[intent_predict]

        # 개체명 파악
        ner_predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)

        # 답변 검색
        try:
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(ner_predicts, answer_text)

        except:
            answer = "죄송합니다. 질문 내용을 이해하지 못했습니다."
            answer_image = None

        json = {
            "Query": query,
            "Answer": answer,
            "AnswerImageUrl": answer_image,
            "Intent": intent_name,
            "NER": str(ner_predicts)
        }

        return json

    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    msg = getMessage('짜장면 두그릇 주문합니다.')
    print(msg)