from chatterbot.trainers import ListTrainer

from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious",logic_adapters=[{'import_path':'chatterbot.logic.BestMatch','threshold':0.65,'default_response':'#'}])

conversation = [
            "你好",
            "你好，我在",
            "最近怎么样？",
            "挺好的",
            "很高兴听到这个",
            "谢谢",
            "不客气"
            ]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("你好")
print(response)
response = chatbot.get_response("最近怎么样")
print(response)
response = chatbot.get_response("很高兴听到")
print(response)
response = chatbot.get_response("谢谢")
print(response)
