from chatbot.Preprocess1 import Preprocess1

sent = "내일 오전 10시에 짜장면 주문하고 싶어요"
p = Preprocess1(userdic='c:/work/python/pyweb2/FoodShop/chatbot/data/user_dic.tsv')

pos = p.pos(sent)
keywords = p.get_keywords(pos, without_tag=False)

print(keywords)
